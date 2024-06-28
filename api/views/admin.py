from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

from itertools import chain

from api import models
from api.utils import MeodelForm_table, pagination
from api.utils.encrypt import md5

# Create your views here.
def departments_first(request):
    se = request.session.get("info", None)
    if se == None:
        departmentsf = {
            "departments": "0000"
        }
    else:
        departmentsf = models.Departments.objects.filter(departments=str(se["id"])[0:4]).first()
    return departmentsf

def departments_name0000():
    departmentsf = {
        "departments": "0000"
    }
    return departmentsf


## 专业列表
def professional_list(request, name):
    '''  专业列表 '''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    if name == 0000:
        departments_list = departments_list.none
        professional_list = departments_list
        departments_name = departments_name0000()
    else:
        # 读取院系名称
        departments_name = models.Departments.objects.filter(departments=name).first()
        # 读取专业所有信息
        professional_list = models.Professional.objects.filter(administrator_departments=name).all()
    page_object = pagination.Pagination(request, professional_list)
    return render(request, 'admin/admin_professional.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": page_object.page_queryset,  # 分完页的数据,
        "departmentsf": departments_first(request),
        "page_string": page_object.html(),  # 生成页码
    })


# 专业添加
def professional_add(request, name):
    if name == 0000:
        messages.info(request, "请先添加学院信息!")
        return redirect("/admin/%d/professional_list/"%name)
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    '''专业添加'''
    professional = MeodelForm_table.MyForm_Professional()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    if request.method == "GET":
        return render(request, 'admin/admin_professional_add.html', {
            "departments_list": departments_list,
            "professional": professional,
            "departments_name": departments_name,
            "departmentsf": departments_first(request),
        })
    date = request.POST
    form = MeodelForm_table.MyForm_Professional(data=date)
    if form.is_valid():
        form.save()
        return redirect("/admin/%d/professional_list/"%name,)

    return render(request, 'admin/admin_professional_add.html', {
        "departments_list": departments_list,
        "departmentsf": departments_first(request),
    })

# 专业修改
def professional_editor(request, name):
    '''编辑专业'''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()

    nid = request.GET.get('nid')
    # 读取专业信息
    professional_list_read = models.Professional.objects.filter(professional=nid).first()
    if request.method == "GET":
        professional_form = MeodelForm_table.MyForm_Professional(instance=professional_list_read)
        return render(request, "admin/admin_professional_editor.html", {
            "departments_list": departments_list,
            "professional_form": professional_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(request),
        })
    professional_form_POST = MeodelForm_table.MyForm_Professional(data=request.POST, instance=professional_list_read)
    if professional_form_POST.is_valid():
        professional_form_POST.save()
        return redirect("/admin/%d/professional_list/"%name,)
    return render(request, "admin/admin_professional_editor.html", {
        "departments_list": departments_list,
        "professional_form": professional_form_POST,
        "departments_name": departments_name,
        "departmentsf": departments_first(request),
    })


# 专业删除
def professional_delete(request, name):
    nid = request.GET.get('nid')
    models.Professional.objects.filter(professional=nid).delete()
    return redirect("/admin/%d/professional_list/"%name,)


## 班级列表
def class_list(request, name):
    ''' 班级列表 '''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    if name == 0000:
        departments_list = departments_list.none()
        class_list_all = departments_list
        departments_name = {
            "departments": "0000",
        }
        professional_list = departments_list
    else:
        departments_name = models.Departments.objects.filter(departments=name).first()
        # 读取专业所有信息
        professional_list = models.Professional.objects.values_list()
        # 读取班级信息

        # 多表实例
        class_list_all = models.Class.objects.filter(professional__administrator_departments=name).all()
    page_object = pagination.Pagination(request, (class_list_all))
    return render(request, 'admin/admin_class.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "class_list_all": page_object.page_queryset,
        "departmentsf": departments_first(request),
        "page_string": page_object.html(),  # 生成页码
    })

# 班级添加
def class_add(request, name):

    if name == 0000:
        messages.info(request, "请先添加专业！")
        return redirect("/admin/%d/class_list/"%name)
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    # 读取专业所有信息
    professional_list = models.Professional.objects.values_list()
    class_adds = MeodelForm_table.MyForm_Class()
    if request.method == "GET":
        return render(request,"admin/admin_class_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "professional_list": professional_list,
            "class_adds": class_adds,
            "departmentsf": departments_first(request),
        })

    date = request.POST
    form = MeodelForm_table.MyForm_Class(data=date)
    if form.is_valid():
        form.save()
        return redirect("/admin/%d/class_list/"%name,)
    return render(request, "admin/admin_class_add.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "class_adds": form,
        "departmentsf": departments_first(request),
    })


# 班级修改
def class_editor(request, name):
    '''编辑班级'''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    nid = request.GET.get('nid')
    # 读取班级信息
    class_list_read = models.Class.objects.filter(classID=nid).first()

    if request.method == "GET":
        class_form = MeodelForm_table.MyForm_Class(instance=class_list_read)
        return render(request, "admin/admin_class_editor.html", {
            "departments_list": departments_list,
            "class_form": class_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(request),
        })
    class_form_POST = MeodelForm_table.MyForm_Class(data=request.POST, instance=class_list_read)
    if class_form_POST.is_valid():
        class_form_POST.save()
        return redirect("/admin/%d/class_list/"%name,)
    return render(request, "admin/admin_class_editor.html", {
        "departments_list": departments_list,
        "class_form": class_form_POST,
        "departments_name": departments_name,
        "departmentsf": departments_first(request),
    })

# 班级删除
def class_delete(request, name):
    nid = request.GET.get('nid')
    models.Class.objects.filter(classID=nid).delete()
    return redirect("/admin/%d/class_list/" %name, )

## 教师列表
def teacher_list(request,name):
    ''' 教师列表 '''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    if name == 0000:
        departments_list = departments_list.none()
        teacher_list_all = departments_list
        departments_name = departments_name0000()
    else:
        # 读取院系名称
        departments_name = models.Departments.objects.filter(departments=name).first()
        # 读取教师所有信息
        teacher_list_all = models.Teacher.objects.filter(teacher_departments=name).all()
    page_object = pagination.Pagination(request, teacher_list_all)

    return render(request, 'admin/admin_teacher.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "teacher_list_all": page_object.page_queryset,
        "departmentsf": departments_first(request),
        "page_string": page_object.html(),  # 生成页码
    })


# 教师添加
def teacher_add(request, name):
    if name == 0000:
        messages.info(request, "请先添加学院")
        return redirect("/admin/%d/teacher_list"%name)
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()

    teacher_adds = MeodelForm_table.MyForm_Teacher()
    if request.method == "GET":
        return render(request, "admin/admin_teacher_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "teacher_adds": teacher_adds,
            "departmentsf": departments_first(request),
        })

    date = request.POST
    form = MeodelForm_table.MyForm_Teacher(data=date)
    if form.is_valid():
        '''职工号'''
        teacher_dep = form.cleaned_data["teacher_departments"]
        departments_sum = models.Teacher.objects.filter(teacher_departments=teacher_dep).all()
        departments_id = models.Departments.objects.filter(departments_name=teacher_dep).values("departments").first()
        teacher_id = len(departments_sum)+1
        lens = len(str(teacher_id))
        if lens == 1:
            teacher_id = "00"+str(teacher_id)
        elif lens == 2:
            teacher_id = "0" + str(teacher_id)
        teacher_id = str(departments_id["departments"])+teacher_id
        form = form.save(commit=False)
        password = md5("Admin0001")
        form.password = password
        form.teacher = teacher_id
        form.save()
        return redirect("/admin/%d/teacher_list/" % name, )
    return render(request, "admin/admin_teacher_add.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "teacher_adds": form,
        "departmentsf": departments_first(request),
    })


# 教师修改
def teacher_editor(request,name):
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    nid = request.GET.get('nid')
    # 读取教师信息
    teacher_list_read = models.Teacher.objects.filter(teacher=nid).first()

    if request.method == "GET":
        teacher_form = MeodelForm_table.MyForm_Teacher(instance=teacher_list_read)
        return render(request, "admin/admin_teacher_editor.html", {
            "departments_list": departments_list,
            "teacher_form": teacher_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(request),
        })
    teacher_form_POST = MeodelForm_table.MyForm_Teacher(data=request.POST, instance=teacher_list_read)
    if teacher_form_POST.is_valid():
        teacher_form_POST.save()
        return redirect("/admin/%d/teacher_list/"%name,)
    return render(request, "admin/admin_teacher_editor.html", {
        "departments_list": departments_list,
        "teacher_form": teacher_form_POST,
        "departments_name": departments_name,
        "departmentsf": departments_first(request),
    })


# 教师删除
def teacher_delete(request, name):
    nid = request.GET.get('nid')
    models.Teacher.objects.filter(teacher=nid).delete()
    return redirect("/admin/%d/teacher_list/" %name, )


## 学生列表
def student(request, name):
    ''' 学生列表 '''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    if name == 0000:
        departments_l = departments_list.none()
        departments_name = {
            "departments": "0000",
        }
        professional_list_all = departments_l
        class_student = departments_l
        class_name = departments_l
    else:
        departments_name = models.Departments.objects.filter(departments=name).first()
        # 读取专业信息
        # 多表实例
        '''反向读取学院的专业'''
        professional_list_all = {}
        for dep in departments_list:
            professional_list_shili = dep.professional_set.all()
            professional_list_all[dep] = professional_list_shili
        # 读取班级学生
        classID = request.GET.get('classID')
        class_student = models.Students.objects.filter(student_class_id=classID).all()
        class_name = models.Class.objects.filter(students__student_class_id=classID).first()
    page_object = pagination.Pagination(request, class_student)

    return render(request, 'admin/admin_student_list.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "professional_list_all": professional_list_all,
        "class_student": page_object.page_queryset,
        "class_name": class_name,
        "departmentsf": departments_first(request),
        "page_string": page_object.html(),  # 生成页码
    })


# 学生班级列表
def student_list(request, name):
    ''' 学生班级列表 '''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    if name == 0000:
        departments_l = departments_list.none()
        departments_name = {
            "departments": "0000",
        }
        professional_list_all = departments_l
        class_list_all = departments_l
    else:
        departments_name = models.Departments.objects.filter(departments=name).first()
        # 读取专业信息
        # 多表实例
        '''{学院:专业}'''
        professional_list_all = {}
        for dep in departments_list:
            professional_list_shili = dep.professional_set.all()
            professional_list_all[dep] = professional_list_shili

        # 多表实例
        '''{专业: 班级}'''
        professional_list_shili = departments_name.professional_set.all()
        class_list_all = models.Class.objects.filter(professional__administrator_departments=name).all()
    page_object = pagination.Pagination(request, class_list_all)
    return render(request, 'admin/admin_student.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "professional_list_all": page_object.page_queryset,
        "class_list_all": class_list_all,
        "departmentsf": departments_first(request),
        "page_string": page_object.html(),  # 生成页码
    })


# 学生添加
def student_add(request, name):
    classsum = models.Class.objects.all()
    if len(classsum) == 0:
        messages.info(request, "请先添加班级！")
        return redirect("/admin/%d/student_list/" % (name), )
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    student_adds = MeodelForm_table.MyForm_Student()
    if request.method == "GET":
        return render(request, "admin/admin_student_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "student_adds": student_adds,
            "departmentsf": departments_first(request),
        })
    # classID = int(request.GET.get("classID"))
    date = request.POST
    student_adds = MeodelForm_table.MyForm_Student(data=date)
    if student_adds.is_valid():

        ''' 编辑学号：学院+专业+班级+序号'''
        '''序号'''
        class_name = student_adds.cleaned_data["student_class"]
        student_id = models.Students.objects.filter(student_class_id=class_name).all()
        student_id = len(student_id) + 1
        if len(str(student_id)) == 1:
            student_id = "0" + str(student_id)
        '''班级'''
        class_dic = models.Class.objects.filter(class_name=class_name).values("classID").first()
        class_id = class_dic["classID"]
        if len(str(class_id)) == 1:
            class_id = "0" + str(class_id)
        '''专业'''
        professional_dic = models.Professional.objects.filter(class__classID=class_dic["classID"]).values(
            "professional").first()
        professional_id = professional_dic["professional"]
        if len(str(professional_id)) == 1:
            professional_id = "0" + str(professional_id)
        '''学院'''
        professional_dict = models.Professional.objects.filter(class__classID=class_dic["classID"]).values(
            "administrator_departments").first()
        departments_dic = models.Departments.objects.filter(
            professional__administrator_departments=professional_dict["administrator_departments"]).values("departments").first()
        departments_id = departments_dic["departments"]
        if len(str(departments_id)) == 1:
            departments_id = "0" + str(departments_id)
        student_id = str(departments_id)+str(professional_id)+str(class_id)+str(student_id)
        '''保存POST没有的字段'''
        student_save = student_adds.save(commit=False)
        student_save.student = student_id
        password = md5(student_id)
        student_save.password = password
        student_save.save()
        return redirect("/admin/%d/student_list/" % (name), )
    return render(request, "admin/admin_student_add.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "student_adds": student_adds,
        "departmentsf": departments_first(request),
    })


# 学生修改
def student_editor(request, name):
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    nid = request.GET.get('nid')
    classID = int(request.GET.get('classID'))
    # 读取学生信息
    student_list_read = models.Students.objects.filter(student=nid).first()

    if request.method == "GET":
        student_form = MeodelForm_table.MyForm_Student(instance=student_list_read)
        return render(request, "admin/admin_student_editor.html", {
            "departments_list": departments_list,
            "student_form": student_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(request),
        })
    student_form_POST = MeodelForm_table.MyForm_Student(data=request.POST, instance=student_list_read)
    if student_form_POST.is_valid():
        student_form_POST.save()
        return redirect("/admin/%d/student_list/" % (name,), )
    return render(request, "admin/admin_student_editor.html", {
        "departments_list": departments_list,
        "student_form": student_form_POST,
        "departments_name": departments_name,
        "departmentsf": departments_first(request),
    })


# 学生删除
def student_delete(request, name):
    classID = int(request.GET.get("classID"))
    nid = request.GET.get('nid')
    models.Students.objects.filter(student=nid).delete()
    return redirect("/admin/%d/student/?classID=%d" %(name, classID), )


## 课程表
def course_list(request, name):
    '''  课程列表 '''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    if name == 0000:
        course_list = departments_list.none()
        departments_name = departments_name0000()
    else:
        # 读取院系名称
        departments_name = models.Departments.objects.filter(departments=name).first()
        # 读取课程所有信息
        course_list = models.Courses.objects.filter(course_departments=name).all()
    page_object = pagination.Pagination(request, course_list)
    return render(request, 'admin/admin_course_list.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "course_list": page_object.page_queryset,
        "departmentsf": departments_first(request),
        "page_string": page_object.html(),  # 生成页码
    })


# 课程添加
def course_add(request, name):
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    if name == 0000:
        messages.info(request, "请先添加学院")
        return redirect("/admin/%d/course_list"%name)
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()

    course_adds = MeodelForm_table.MyForm_Courses()
    if request.method == "GET":
        return render(request, "admin/admin_course_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "course_adds": course_adds,
            "departmentsf": departments_first(request),
        })

    date = request.POST
    form = MeodelForm_table.MyForm_Courses(data=date)
    if form.is_valid():
        form.save()
        return redirect("/admin/%d/course_list/" % name, )
    return render(request, "admin/admin_course_add.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "course_adds": form,
        "departmentsf": departments_first(request),
    })


# 课程删除
def course_delete(request, name):
    nid = request.GET.get('nid')
    models.Courses.objects.filter(course=nid).delete()
    return redirect("/admin/%d/course_list/" %(name), )


# 课程修改
def course_editor(request, name):
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    nid = request.GET.get("nid")
    course_list_read = models.Courses.objects.filter(course=nid).first()
    if request.method == "GET":
        course_adds = MeodelForm_table.MyForm_Courses(instance=course_list_read)
        return render(request, "admin/admin_course_editor.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "course_adds": course_adds,
            "departmentsf": departments_first(request),
        })
    date = request.POST
    form = MeodelForm_table.MyForm_Courses(data=date, instance=course_list_read)
    if form.is_valid():
        form.save()
        return redirect("/admin/%d/course_list/" % name, )
    return render(request, "admin/admin_course_editor.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "course_adds": form,
        "departmentsf": departments_first(request),
    })




## 管理员信息
def admin(request, name):
    # 读取院系所有信息
    departments_list = models.Departments.objects.filter(departments=name).first()
    session_id = request.session.get("info", None)
    admin_admin = models.Administrator.objects.filter(administrator=session_id["id"]).first()
    return render(request, "admin/admin_admin.html", {
        "admin_admin": admin_admin,
        "departments_list": departments_list,
        "departmentsf": departments_first(request),
    })


def admin_pwd(request, name):
    if request.method == "GET":
        form = MeodelForm_table.PWDeditor()
        return render(request, "admin/admin_admin_pwd.html", {
            "form": form,
            "departmentsf": departments_first(request),
        })
    form = MeodelForm_table.PWDeditor(data=request.POST)
    if form.is_valid():
        nid = request.GET.get("nid")
        # 原密码的校验
        form_password = form.cleaned_data['password']
        password = models.Administrator.objects.filter(administrator=nid).values("password").first()
        password = password["password"]
        nid = int(nid)
        if password != md5(form_password):
            messages.info(request, "原密码错误！")
            return redirect("/admin/%d/admin_pwd/?nid=%d"%(name,nid))
        elif form.cleaned_data['new_password'] != form.cleaned_data["con_password"]:
            messages.info(request, "密码不一致！")
            return redirect("/admin/%d/admin_pwd/?nid=%d"%(name,nid))
        else:
            new_password = md5(form.cleaned_data['new_password'])
            models.Administrator.objects.filter(administrator=nid).update(password=new_password)
            messages.info(request, "修改成功！")
            return redirect("/admin/%d/admin/"%name)
    return render(request, "admin/admin_admin_pwd.html", {
        "form": form,
        "departmentsf": departments_first(request),
    })


# 授课表
def teaching_list(request, name):
    departments_name = models.Departments.objects.filter(departments=name).first()
    teacher_db = models.Teaching.objects.filter(course__course_departments=name).all()
    page_object = pagination.Pagination(request, teacher_db)
    return render(request, "admin/admin_teaching_list.html", {
        "departmentsf": departments_first(request),
        "departments_name": departments_name,
        "teaching_all" : page_object.page_queryset,
        "page_string": page_object.html(),  # 生成页码
    })


# 授课表添加
def teaching_add(request, name):
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    teaching_adds = MeodelForm_table.MyForm_Teaching()
    if request.method == "GET":
        return render(request, "admin/admin_teaching_add.html", {
            "departments_name": departments_name,
            "teaching_adds": teaching_adds,
            "departmentsf": departments_first(request),
        })
    date = request.POST
    form = MeodelForm_table.MyForm_Teaching(data=date)
    if form.is_valid():
        form.save()
        return redirect("/admin/%d/teaching_list/" % name, {
            "teaching_adds": form,
            "departmentsf": departments_first(request),
        })
    return render(request, "admin/admin_teaching_add.html", {
        "departmentsf": departments_first(request),
        "teaching_adds": form,
    })


# 授课表修改
def teaching_editor(request, name):
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()

    nid = request.GET.get("nid")
    teaching_list_read = models.Teaching.objects.filter(id=nid).first()
    if request.method == "GET":
        teaching_adds = MeodelForm_table.MyForm_Teaching(instance=teaching_list_read)
        return render(request, "admin/admin_teaching_editor.html", {
            "departments_name": departments_name,
            "teaching_adds": teaching_adds,
            "departmentsf": departments_first(request),
        })

    date = request.POST
    form = MeodelForm_table.MyForm_Teaching(data=date, instance=teaching_list_read)
    if form.is_valid():
        form.save()
        return redirect("/admin/%d/teaching_list/" % name, {
            "departmentsf": departments_first(request),
        })

    return render(request, "admin/admin_teaching_editor.html", {
        "departmentsf": departments_first(request),
        "teaching_adds": form,
    })


# 授课表删除
def teaching_delete(request, name):
    nid = request.GET.get('nid')
    models.Teaching.objects.filter(id=nid).delete()
    return redirect("/admin/%d/teaching_list/" %(name), )


# 班级课程表
def class_course_list(request, name):
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    class_course = models.Class_course.objects.filter(course__course_departments=name).all()
    return render(request, "admin/admin_class_course.html", {
        "departmentsf": departments_first(request),
        "departments_name": departments_name,
        "class_course": class_course,
    })


def class_course_add(request, name):
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    class_course_adds = MeodelForm_table.MyForm_Class_course()
    if request.method == "GET":
        return render(request, "admin/admin_class_course_add.html", {
            "departments_name": departments_name,
            "class_course_adds": class_course_adds,
            "departmentsf": departments_first(request),
        })
    data = request.POST
    form = MeodelForm_table.MyForm_Class_course(data=data)
    if form.is_valid():
        form.save()
        class_name = form.cleaned_data["classid"]
        course_name = form.cleaned_data["course"]
        class_id = models.Class.objects.filter(class_name=class_name).first()
        student_id = models.Students.objects.filter(student_class=class_id).all()
        student_a = models.Students.objects.filter(student_class=class_id).values("student").first()
        for i in student_id:
            models.Electives.objects.create(course=course_name, student=i)

        return redirect("/admin/%d/class_course_list/" % name, {
            "departmentsf": departments_first(request),
        })

    return render(request, "admin/admin_class_course_add.html", {
        "departmentsf": departments_first(request),
        "departments_name": departments_name,
        "class_course_adds": form,
    })


def class_course_editor(request, name):
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    nid = request.GET.get("nid")
    class_course_rad = models.Class_course.objects.filter(id=nid).first()
    if request.method == "GET":
        class_course_adds = MeodelForm_table.MyForm_Class_course(instance=class_course_rad)
        return render(request, "admin/admin_class_course_editor.html", {
            "departments_name": departments_name,
            "class_course_adds": class_course_adds,
            "departmentsf": departments_first(request),
        })
    date = request.POST
    form = MeodelForm_table.MyForm_Class_course(data=date, instance=class_course_rad)
    if form.is_valid():
        form.save()
        return redirect("/admin/%d/class_course_list/" % name, )
    return render(request, "admin/admin_class_course_editor.html", {
        "departmentsf": departments_first(request),
        "departments_name": departments_name,
    })



def class_course_delete(request, name):
    nid = request.GET.get("nid")
    models.Class_course.objects.filter(id=nid).delete()
    return redirect("/admin/%d/class_course_list/" % name, )

# 搜索
def search(request, name):
    if request.method == "GET":
        messages.info(request, "请输入内容进行搜索！")
    elif request.method == "POST":
        search_input = request.POST.get("search")
        if search_input == "":
            return render(request, "admin/admin_search_none.html", {
                "departmentsf": departments_first(request),
            },)
        elif search_input.isdigit():
            student_id = models.Students.objects.filter(student=search_input).first()
            teacher_id = models.Teacher.objects.filter(teacher=search_input).first()
            if student_id != None:
                student_class = models.Students.objects.filter(student=search_input).values("student_class").first()
                class_id = models.Class.objects.filter(students__student=search_input).values("classID").first()
                departments_name = models.Professional.objects.filter(class__classID=student_class["student_class"]).values("administrator_departments").first()
                search = student_id
                if departments_name["administrator_departments"] == name:
                    return render(request, "admin/admin_search_student.html", {
                        "departmentsf": departments_first(request),
                        "searchs": search,
                        "departments_name": departments_name,
                        "class_id": class_id,
                    },
                    )
                else:
                    return render(request, "admin/admin_search_none.html", {
                        "departmentsf": departments_first(request),
                    },
                                  )
            elif teacher_id != None:
                departments_name = models.Departments.objects.filter(teacher__teacher=search_input).values("departments").first()
                search = teacher_id
                if departments_name["departments"] == name:
                    return render(request, "admin/admin_search_teacher.html", {
                        "departmentsf": departments_first(request),
                        "searchs": search,
                        "departments_name": departments_name,
                    },
                    )
                else:
                    return render(request, "admin/admin_search_none.html", {
                        "departmentsf": departments_first(request),
                    },
                                  )
            else:
                return render(request, "admin/admin_search_none.html", {
                    "departmentsf": departments_first(request),
                },
                )
        else:
            student_name = models.Students.objects.filter(student_name=search_input).first()
            teacher_name = models.Teacher.objects.filter(teacher_name=search_input).first()
            if student_name != None:
                student_class = models.Students.objects.filter(student_name=search_input).values("student_class").first()
                class_id = models.Class.objects.filter(students__student_name=search_input).values("classID").first()
                departments_name = models.Professional.objects.filter(class__classID=student_class["student_class"]).values("administrator_departments").first()
                search = student_name
                if departments_name["administrator_departments"] == name:
                    return render(request, "admin/admin_search_student.html", {
                        "departmentsf": departments_first(request),
                        "searchs": search,
                        "departments_name": departments_name,
                        "class_id": class_id,
                    },
                    )
                else:
                    return render(request, "admin/admin_search_none.html", {
                        "departmentsf": departments_first(request),
                    },
                                  )
            elif teacher_name != None:
                departments_name = models.Departments.objects.filter(teacher__teacher_name=search_input).values("departments").first()
                search = teacher_name
                if departments_name["departments"] == name:
                    return render(request, "admin/admin_search_teacher.html", {
                        "departmentsf": departments_first(request),
                        "searchs": search,
                        "departments_name": departments_name,
                    },
                    )
                else:
                    return render(request, "admin/admin_search_none.html", {
                        "departmentsf": departments_first(request),
                    },
                                  )
            else:
                return render(request, "admin/admin_search_none.html", {
                    "departmentsf": departments_first(request),
                },
                )
