from django.shortcuts import render, redirect
from django.contrib import messages

from itertools import chain

from api import models
from api.utils import MeodelForm_table, pagination
from api.utils.encrypt import md5


# 教师
def teacher_list(request, name):
    print(name)
    teacher_all = models.Teacher.objects.filter(teacher=name).all()
    return render(request, "teacher/teacher_list.html", {
        "name": name,
        "teacher_all": teacher_all,
    })


# 成绩登记
def teacher_electives(request, name):
    course_list = models.Teaching.objects.filter(teacher=name).all()
    course_l = course_list.values("course")
    electives_all = course_list.none()
    for i in course_l:
        course = i["course"]
        electives = models.Electives.objects.filter(course=course).all()
        electives_all = chain(electives_all,electives)
    return render(request, "teacher/teacher_elective.html", {
        "name": name,
        "course_list": course_list,
        "electives_all": electives_all,
    })


# 登记成绩
def registration(request, name):
    nid = request.GET.get("nid")
    electives_list = models.Electives.objects.filter(electives=nid).first()
    studnet_list = models.Students.objects.filter(electives__electives=nid).first()
    if request.method == "GET":
        form = MeodelForm_table.MyForm_Electives(instance=electives_list)
        return render(request, "teacher/teacher_registration.html", {
            "name": name,
            "form": form,
            "studnet_list": studnet_list,
        })
    date = request.POST
    form_POST = MeodelForm_table.MyForm_Electives(data=date, instance=electives_list)
    if form_POST.is_valid():
        form_POST.save()
        return redirect("/teacher/%d/teacher_electives/" % name, )
    return render(request, "teacher/teacher_registration.html", {
        "form": form_POST,
        "name": name,
        "studnet_list": studnet_list,
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

