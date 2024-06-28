from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages



from itertools import chain

from api import models
from api.utils import MeodelForm_table, pagination
from api.utils.encrypt import md5

# Create your views here.
def departments_first():
    departmentsf = models.Departments.objects.first()
    if departmentsf == None:
        departmentsf = {
            "departments": "0000"
        }
    return departmentsf

def departments_name0000():
    departmentsf = {
        "departments": "0000"
    }
    return departmentsf

def ceshi(request):
    return render(request,"ceshi.html")


## 院系列表
def departments_list(request):
    '''  院系列表 '''
    # 读取院系所有信息
    departments_list_read = models.Departments.objects.all()

    page_object = pagination.Pagination(request, departments_list_read)
    return render(request, 'root/root_departments.html', {
        "departments_list" : page_object.page_queryset,
        "page_string": page_object.html(),  # 生成页码
        "departmentsf": departments_first(),
    })

# 院系添加
def departments_add(request):
    # 读取院系所有信息
    # departments_list_read = models.Departments.objects.all()
    '''添加院系'''
    departments = MeodelForm_table.MyForm_Departments()
    if request.method == "GET":
        return render(request, 'root/root_departments_add.html', {
            "departments" : departments,
            "departmentsf": departments_first(),
        })
    # 获取院系名称
    departments = MeodelForm_table.MyForm_Departments(data=request.POST)
    if departments.is_valid():
        departments.save()
        return redirect("/root/departments_list/", {
            "departmentsf": departments_first(),
        })
    # 回显错误信息
    return render(request, 'root/root_departments_add.html', {
        "departments": departments,
        "departmentsf": departments_first(),
    })

# 院系修改
def departments_editor(request):
    '''编辑院系'''
    nid = request.GET.get("nid")
    departments_ID = models.Departments.objects.filter(departments=nid).first()
    departments_form = MeodelForm_table.MyForm_Departments(instance=departments_ID)

    if request.method == "GET":
        return render(request, 'root/root_departments_editor.html', {
            "departments_form" : departments_form,
            "departmentsf": departments_first(),
        })

    # 保存到数据库
    departments_name = MeodelForm_table.MyForm_Departments(data=request.POST, instance=departments_ID)
    if departments_name.is_valid():
        departments_name.save()
        return redirect("/root/departments_list/", {
            "departmentsf": departments_first(),
        })


    return redirect("/root/departments_list/", {
        "departments_form": departments_name,
        "departmentsf": departments_first(),
    })

# 院系删除
def departments_delete(request):
    nid = request.GET.get('nid')
    models.Departments.objects.filter(departments=nid).delete()
    # tables_sql.Departments_interaction.delete(nid)
    return redirect("/root/departments_list/")


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
    return render(request, 'root/root_professional.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": page_object.page_queryset,  # 分完页的数据,
        "departmentsf": departments_first(),
        "page_string": page_object.html(),  # 生成页码
    })


# 专业添加
def professional_add(request, name):
    if name == 0000:
        messages.info(request, "请先添加学院信息!")
        return redirect("/root/%d/professional_list/"%name)
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    '''专业添加'''
    professional = MeodelForm_table.MyForm_Professional()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    if request.method == "GET":
        return render(request, 'root/root_professional_add.html', {
            "departments_list": departments_list,
            "professional": professional,
            "departments_name": departments_name,
            "departmentsf": departments_first(),
        })
    date = request.POST
    form = MeodelForm_table.MyForm_Professional(data=date)
    if form.is_valid():
        form.save()
        return redirect("/root/%d/professional_list/"%name,)

    return render(request, 'root/root_professional_add.html', {
        "professional": form,
        "departments_list": departments_list,
        "departmentsf": departments_first(),
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
        return render(request, "root/root_professional_editor.html", {
            "departments_list": departments_list,
            "professional_form": professional_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(),
        })
    professional_form_POST = MeodelForm_table.MyForm_Professional(data=request.POST, instance=professional_list_read)
    if professional_form_POST.is_valid():
        professional_form_POST.save()
        return redirect("/root/%d/professional_list/"%name,)
    return render(request, "root/root_professional_editor.html", {
        "departments_list": departments_list,
        "professional_form": professional_form_POST,
        "departments_name": departments_name,
        "departmentsf": departments_first(),
    })


# 专业删除
def professional_delete(request, name):
    nid = request.GET.get('nid')
    models.Professional.objects.filter(professional=nid).delete()
    return redirect("/root/%d/professional_list/"%name,)


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
    return render(request, 'root/root_class.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "class_list_all": page_object.page_queryset,
        "departmentsf": departments_first(),
        "page_string": page_object.html(),  # 生成页码
    })

# 班级添加
def class_add(request, name):

    if name == 0000:
        messages.info(request, "请先添加专业！")
        return redirect("/root/%d/class_list/"%name)
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    # 读取专业所有信息
    professional_list = models.Professional.objects.values_list()
    class_adds = MeodelForm_table.MyForm_Class()
    if request.method == "GET":
        return render(request,"root/root_class_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "professional_list": professional_list,
            "class_adds": class_adds,
            "departmentsf": departments_first(),
        })

    date = request.POST
    form = MeodelForm_table.MyForm_Class(data=date)
    if form.is_valid():
        form.save()
        return redirect("/root/%d/class_list/"%name,)
    return render(request, "root/root_class_add.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "class_adds": form,
        "departmentsf": departments_first(),
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
        return render(request, "root/root_class_editor.html", {
            "departments_list": departments_list,
            "class_form": class_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(),
        })
    class_form_POST = MeodelForm_table.MyForm_Class(data=request.POST, instance=class_list_read)
    if class_form_POST.is_valid():
        class_form_POST.save()
        return redirect("/root/%d/class_list/"%name,)
    return render(request, "root/root_class_editor.html", {
        "departments_list": departments_list,
        "class_form": class_form_POST,
        "departments_name": departments_name,
        "departmentsf": departments_first(),
    })

# 班级删除
def class_delete(request, name):
    nid = request.GET.get('nid')
    models.Class.objects.filter(classID=nid).delete()
    return redirect("/root/%d/class_list/" %name, )

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

    return render(request, 'root/root_teacher.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "teacher_list_all": page_object.page_queryset,
        "departmentsf": departments_first(),
        "page_string": page_object.html(),  # 生成页码
    })


# 教师添加
def teacher_add(request, name):
    if name == 0000:
        messages.info(request, "请先添加学院")
        return redirect("/root/%d/teacher_list"%name)
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()

    teacher_adds = MeodelForm_table.MyForm_Teacher()
    if request.method == "GET":
        return render(request, "root/root_teacher_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "teacher_adds": teacher_adds,
            "departmentsf": departments_first(),
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
        return redirect("/root/%d/teacher_list/" % name, )
    return render(request, "root/root_teacher_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "teacher_adds": form,
            "departmentsf": departments_first(),
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
        return render(request, "root/root_teacher_editor.html", {
            "departments_list": departments_list,
            "teacher_form": teacher_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(),
        })
    teacher_form_POST = MeodelForm_table.MyForm_Teacher(data=request.POST, instance=teacher_list_read)
    if teacher_form_POST.is_valid():
        teacher_form_POST.save()
        return redirect("/root/%d/teacher_list/"%name,)
    return render(request, "root/root_teacher_editor.html", {
            "departments_list": departments_list,
            "teacher_form": teacher_form_POST,
            "departments_name": departments_name,
            "departmentsf": departments_first(),
        })


# 教师删除
def teacher_delete(request, name):
    nid = request.GET.get('nid')
    models.Teacher.objects.filter(teacher=nid).delete()
    return redirect("/root/%d/teacher_list/" %name, )


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

    return render(request, 'root/root_student_list.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "professional_list_all": professional_list_all,
        "class_student": page_object.page_queryset,
        "class_name": class_name,
        "departmentsf": departments_first(),
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
    return render(request, 'root/root_student.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "professional_list": professional_list,
        "professional_list_all": page_object.page_queryset,
        "class_list_all": class_list_all,
        "departmentsf": departments_first(),
        "page_string": page_object.html(),  # 生成页码
    })


# 学生添加
def student_add(request, name):
    classsum = models.Class.objects.all()
    if len(classsum) == 0:
        messages.info(request, "请先添加班级！")
        return redirect("/root/%d/student_list/" % (name), )
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()
    student_adds = MeodelForm_table.MyForm_Student()

    if request.method == "GET":
        return render(request, "root/root_student_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "student_adds": student_adds,
            "departmentsf": departments_first(),
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
        return redirect("/root/%d/student_list/" % (name), )
    return render(request, "root/root_student_add.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "student_adds": student_adds,
        "departmentsf": departments_first(),
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
        return render(request, "root/root_student_editor.html", {
            "departments_list": departments_list,
            "student_form": student_form,
            "departments_name": departments_name,
            "departmentsf": departments_first(),
        })
    student_form_POST = MeodelForm_table.MyForm_Student(data=request.POST, instance=student_list_read)
    if student_form_POST.is_valid():
        student_form_POST.save()
        return redirect("/root/%d/student_list/" % (name,), )
    return render(request, "root/root_student_editor.html", {
            "departments_list": departments_list,
            "student_form": student_form_POST,
            "departments_name": departments_name,
            "departmentsf": departments_first(),
        })


# 学生删除
def student_delete(request, name):
    classID = int(request.GET.get("classID"))
    nid = request.GET.get('nid')
    models.Students.objects.filter(student=nid).delete()
    return redirect("/root/%d/student/?classID=%d" %(name, classID), )


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
    return render(request, 'root/root_course_list.html', {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "course_list": page_object.page_queryset,
        "departmentsf": departments_first(),
        "page_string": page_object.html(),  # 生成页码
    })


# 课程添加
def course_add(request, name):
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    if name == 0000:
        messages.info(request, "请先添加学院")
        return redirect("/root/%d/course_list"%name)
    # 读取院系名称
    departments_name = models.Departments.objects.filter(departments=name).first()

    course_adds = MeodelForm_table.MyForm_Courses()
    if request.method == "GET":
        return render(request, "root/root_course_add.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "course_adds": course_adds,
            "departmentsf": departments_first(),
        })

    date = request.POST
    form = MeodelForm_table.MyForm_Courses(data=date)
    if form.is_valid():
        form.save()
        return redirect("/root/%d/course_list/" % name, )
    return render(request, "root/root_course_add.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "course_adds": form,
        "departmentsf": departments_first(),
    })


# 课程删除
def course_delete(request, name):
    nid = request.GET.get('nid')
    models.Courses.objects.filter(course=nid).delete()
    return redirect("/root/%d/course_list/" %(name), )


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
        return render(request, "root/root_course_editor.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "course_adds": course_adds,
            "departmentsf": departments_first(),
        })
    date = request.POST
    form = MeodelForm_table.MyForm_Courses(data=date, instance=course_list_read)
    if form.is_valid():
        form.save()
        return redirect("/root/%d/course_list/" % name, )
    return render(request, "root/root_course_editor.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "course_adds": form,
        "departmentsf": departments_first(),
    })



## 系统管理
def system_man(request):
    # 读取院系管理员
    departments_admin = models.Administrator.objects.all()
    page_object = pagination.Pagination(request, departments_admin)
    return render(request, "root/system.html", {
        "departments_admin": page_object.page_queryset,
        "departmentsf": departments_first(),
        "page_string": page_object.html(),  # 生成页码
    })


# 管理员添加
def system_man_add(request):
    '''添加院系管理员'''
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()
    administrator_add = MeodelForm_table.MyForm_Administrator()
    if  len(departments_list)== 0:
        messages.info(request, "请先添加学院")
        return redirect("/root/system_man/")
    if request.method == "GET":
        return render(request, 'root/system_add.html', {
            "administrator_add" : administrator_add,
            "departmentsf": departments_first(),
        })
    # 获取院系名称
    administrator_add = MeodelForm_table.MyForm_Administrator(data=request.POST)

    if administrator_add.is_valid():
        Departments_id = administrator_add.cleaned_data["administrator_departments"]
        administrator_id = models.Departments.objects.filter(departments_name=Departments_id).values("departments").first()
        administrator_sum = models.Administrator.objects.filter(administrator_departments=administrator_id["departments"]).all()
        administrator_sum = len(administrator_sum)
        administrator_add = administrator_add.save(commit=False)
        administratorID = str(administrator_id["departments"])+str(administrator_sum)
        password = md5("admin")
        administrator_add.administrator = administratorID
        administrator_add.password = password
        administrator_add.save()
        return redirect("/root/system_man/")
    # 回显错误信息
    return render(request, 'root/system_add.html', {
        "administrator_add": administrator_add,
        "departmentsf": departments_first(),
    })


# 管理员删除
def system_man_delete(request):
    nid = request.GET.get('nid')
    models.Administrator.objects.filter(administrator=nid).delete()
    return redirect("/root/system_man/",)


# 管理员密码重置
def system_man_password(request):
    nid = request.GET.get("nid")
    password = md5("admin")
    models.Administrator.objects.filter(administrator=nid).update(password=password)
    messages.info(request, "重置成功！")
    return redirect("/root/system_man/")


# 管理员修改
def system_man_editor(request):
    nid = request.GET.get("nid")
    # 读取院系名称
    departments_name = models.Departments.objects.filter(administrator__administrator=nid).first()
    administrator_list_read = models.Administrator.objects.filter(administrator=nid).first()
    if request.method == "GET":
        administrator_adds = MeodelForm_table.MyForm_Administrator(instance=administrator_list_read)
        return render(request, "root/system_editor.html", {
            "departments_list": departments_list,
            "departments_name": departments_name,
            "administrator_adds": administrator_adds,
            "departmentsf": departments_first(),
        })
    date = request.POST
    form = MeodelForm_table.MyForm_Administrator(data=date, instance=administrator_list_read)
    if form.is_valid():
        form.save()
        return redirect("/root/system_man/")
    return render(request, "root/system_editor.html", {
        "departments_list": departments_list,
        "departments_name": departments_name,
        "administrator_adds": form,
        "departmentsf": departments_first(),
    })

# 选课管理
def course_selection(request, name):
    course_first = models.Course_selection.objects.first()
    if request.method == "GET":
        course_form = MeodelForm_table.MyForm_Course_selection(instance=course_first)
        return render(request, "root/root_course_selection.html", {
            "departmentsf": departments_first(),
            "form": course_form,
        })
    data = request.POST
    course_form = MeodelForm_table.MyForm_Course_selection(data=data, instance=course_first)
    if course_form:
        course_form.save()
        messages.info(request, "修改成功！")
        return render(request, "root/root_course_selection.html", {
            "departmentsf": departments_first(),
            "form": course_form,
        })
    render(request, "root/root_course_selection.html", {
        "departmentsf": departments_first(),
        "form": course_form,
    })


## 超级管理员
def admin(request):
    # 读取院系所有信息
    departments_list = models.Departments.objects.all()

    root_admin = models.Root.objects.first()
    return render(request, "root/root_admin.html", {
        "root_admin": root_admin,
        "departments_list": departments_list,
        "departmentsf": departments_first(),
    })


def admin_pwd(request):
    if request.method == "GET":
        form = MeodelForm_table.PWDeditor()
        return render(request, "root/root_admin_pwd.html", {
            "form": form,
        })
    form = MeodelForm_table.PWDeditor(data=request.POST)
    if form.is_valid():
        nid = request.GET.get("nid")
        # 原密码的校验
        form_password = form.cleaned_data['password']
        password = models.Root.objects.filter(id=nid).values("password").first()
        password = password["password"]
        nid = int(nid)
        if password != md5(form_password):
            messages.info(request, "原密码错误！")
            return redirect("/admin_pwd/?nid=%d"%nid)
        elif form.cleaned_data['new_password'] != form.cleaned_data["con_password"]:
            messages.info(request, "密码不一致！")
            return redirect("/admin_pwd/?nid=%d"%nid)
        else:
            new_password = md5(form.cleaned_data['new_password'])
            models.Root.objects.filter(id=nid).update(password=new_password)
            messages.info(request, "修改成功！")
            return redirect("/admin/")
    return render(request, "root/root_admin_pwd.html", {
        "form": form,
    })


# 搜索
def search(request):
    if request.method == "GET":
        messages.info(request, "请输入内容进行搜索！")
    elif request.method == "POST":
        search_input = request.POST.get("search")
        if search_input == "":
            return render(request, "root/root_search_none.html", {
                "departmentsf": departments_first(),
            },)
        elif search_input.isdigit():

            student_id = models.Students.objects.filter(student=search_input).first()
            teacher_id = models.Teacher.objects.filter(teacher=search_input).first()
            if student_id != None:
                student_class = models.Students.objects.filter(student=search_input).values("student_class").first()
                class_id = models.Class.objects.filter(students__student=search_input).values("classID").first()
                departments_name = models.Professional.objects.filter(class__classID=student_class["student_class"]).values("administrator_departments").first()
                search = student_id
                return render(request, "root/root_search_student.html", {
                    "departmentsf": departments_first(),
                    "searchs": search,
                    "departments_name": departments_name,
                    "class_id": class_id,
                },
                )
            elif teacher_id != None:
                departments_name = models.Departments.objects.filter(teacher__teacher=search_input).first()
                search = teacher_id
                return render(request, "root/root_search_teacher.html", {
                    "departmentsf": departments_first(),
                    "searchs": search,
                    "departments_name": departments_name,
                },
                )
            else:
                return render(request, "root/root_search_none.html", {
                    "departmentsf": departments_first(),
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
                return render(request, "root/root_search_student.html", {
                    "departmentsf": departments_first(),
                    "searchs": search,
                    "departments_name": departments_name,
                    "class_id": class_id,
                },
                )
            elif teacher_name != None:
                departments_name = models.Departments.objects.filter(teacher__teacher_name=search_input).first()
                search = teacher_name
                return render(request, "root/root_search_teacher.html", {
                    "departmentsf": departments_first(),
                    "searchs": search,
                    "departments_name": departments_name,
                },
                )
            else:
                return render(request, "root/root_search_none.html", {
                    "departmentsf": departments_first(),
                },
                )
