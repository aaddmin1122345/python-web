from django.shortcuts import render, redirect
from django.contrib import messages

from api import models
from api.utils import MeodelForm_table, pagination
from api.utils.encrypt import md5


# 学生
def student_list(request, name):
    print(name)
    student_all = models.Students.objects.filter(student=name).all()
    return render(request, "student/student_list.html", {
        "name": name,
        "student_all": student_all,
    })


# 课程表
def course(request, name):
    course_list = models.Electives.objects.filter(student=name).all()
    return render(request, "student/student_course.html", {
        "name": name,
        "course_list": course_list,
    })


# 成绩单
def results(request, name):
    course_list = models.Electives.objects.filter(student=name).all()
    return render(request, "student/student_results.html", {
        "name": name,
        "course_list": course_list,
    })


# 选课
def choose(request, name):
    course_selection = models.Course_selection.objects.values("course").first()
    print(course_selection)
    if course_selection["course"] == 1:
        courses_all = models.Courses.objects.filter(course_choose=1).values_list()
        li = []
        for i in courses_all:
            courseid = i[0]
            course_name = i[1]
            course_list = [courseid, course_name]
            li.append(course_list)
        # course_tuple = tuple(li)
        if request.method == "GET":
            return render(request, "student/student_choose.html", {
                "name": name,
                "course_tuple": li,
            })
        date = request.POST
        student_id = name
        course_id = date.get("paymentMethod")
        student_id = models.Students.objects.get(student=student_id)
        course_id = models.Courses.objects.get(course=course_id)
        models.Electives.objects.create(student=student_id, course=course_id, course_results=0)
        messages.info(request, "选课完成！")
        return render(request, "student/student_choose_no.html", {
            "name": name,
            "course_tuple": date,
        })
    return render(request, "student/student_choose_no.html", {
        "name": name,
    })

# 修改密码
def pwd(request, name):
    if request.method == "GET":
        form = MeodelForm_table.PWDeditor()
        return render(request, "student/student_pwd.html", {
            "name": name,
            "form": form,
        })
    form = MeodelForm_table.PWDeditor(data=request.POST)
    if form.is_valid():
        # 原密码的校验
        form_password = form.cleaned_data['password']
        password = models.Students.objects.filter(student=name).values("password").first()
        password = password["password"]
        nid = int(name)
        if password != md5(form_password):
            messages.info(request, "原密码错误！")
            return redirect("/student/%d/pwd/"%(name))
        elif form.cleaned_data['new_password'] != form.cleaned_data["con_password"]:
            messages.info(request, "密码不一致！")
            return redirect("/student/%d/pwd/"%(name))
        else:
            new_password = md5(form.cleaned_data['new_password'])
            models.Students.objects.filter(student=nid).update(password=new_password)
            messages.info(request, "修改成功！")
            return redirect("/student/%d/pwd/"%(name))
    return render(request, "student/pwd.html", {
        "name": name,
        "form": form,
    })

