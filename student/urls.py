"""students_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import root, admin, student, teacher, account

urlpatterns = [
    path('ceshi/', root.ceshi),

    # 注销
    path('logout/', account.logout),

    path('sql/', account.sql),
    ## 后台登陆  account
    path('root_login/', account.root_login),
    path('img/code/', account.image_code),  # 验证码

    ## 超级管理员 root
    # 院系表
    path('root/departments_list/', root.departments_list),
    path('root/departments_add/', root.departments_add),
    path('root/departments_editor/', root.departments_editor),
    path('root/departments_delete/', root.departments_delete),

    # 专业表
    path('root/<int:name>/professional_list/', root.professional_list),
    path('root/<int:name>/professional_add/', root.professional_add),
    path('root/<int:name>/professional_editor/', root.professional_editor),
    path('root/<int:name>/professional_delete/', root.professional_delete),

    # 班级表
    path('root/<int:name>/class_list/', root.class_list),
    path('root/<int:name>/class_add/', root.class_add),
    path('root/<int:name>/class_editor/', root.class_editor),
    path('root/<int:name>/class_delete/', root.class_delete),

    # 教师   teacher
    path('root/<int:name>/teacher_list/', root.teacher_list),
    path('root/<int:name>/teacher_add/', root.teacher_add),
    path('root/<int:name>/teacher_editor/', root.teacher_editor),
    path('root/<int:name>/teacher_delete/', root.teacher_delete),

    # 学生   student
    path('root/<int:name>/student/', root.student),
    path('root/<int:name>/student_list/', root.student_list),
    path('root/<int:name>/student_add/', root.student_add),
    path('root/<int:name>/student_editor/', root.student_editor),
    path('root/<int:name>/student_delete/', root.student_delete),

    # 课程表 course
    path('root/<int:name>/course_list/', root.course_list),
    path('root/<int:name>/course_add/', root.course_add),
    path('root/<int:name>/course_editor/', root.course_editor),
    path('root/<int:name>/course_delete/', root.course_delete),

    # 选课管理
    path('root/<int:name>/course_selection/', root.course_selection),

    # 系统管理
    path('root/system_man/', root.system_man),
    path('root/system_man_add/', root.system_man_add),
    path('root/system_man_delete/', root.system_man_delete),
    path('root/system_man_password/', root.system_man_password),
    path('root/system_man_editor/', root.system_man_editor),

    path('root/admin/', root.admin),  # 个人信息显示
    path('root/admin_pwd/', root.admin_pwd),
    ## 院系管理员  admin

    ## 系统登陆  account
    path('login/', account.login),
    path('img/code/', account.image_code),  # 验证码
    path('con_pwd/', account.pwd_mail),  # 找回密码
    path('email/', account.email),

    # 搜索
    path("root/search/", root.search),

    ## 院系管理员

    # 专业表
    path('admin/<int:name>/professional_list/', admin.professional_list),
    path('admin/<int:name>/professional_add/', admin.professional_add),
    path('admin/<int:name>/professional_editor/', admin.professional_editor),
    path('admin/<int:name>/professional_delete/', admin.professional_delete),

    # 班级表
    path('admin/<int:name>/class_list/', admin.class_list),
    path('admin/<int:name>/class_add/', admin.class_add),
    path('admin/<int:name>/class_editor/', admin.class_editor),
    path('admin/<int:name>/class_delete/', admin.class_delete),

    # 教师   teacher
    path('admin/<int:name>/teacher_list/', admin.teacher_list),
    path('admin/<int:name>/teacher_add/', admin.teacher_add),
    path('admin/<int:name>/teacher_editor/', admin.teacher_editor),
    path('admin/<int:name>/teacher_delete/', admin.teacher_delete),

    # 学生   student
    path('admin/<int:name>/student/', admin.student),
    path('admin/<int:name>/student_list/', admin.student_list),
    path('admin/<int:name>/student_add/', admin.student_add),
    path('admin/<int:name>/student_editor/', admin.student_editor),
    path('admin/<int:name>/student_delete/', admin.student_delete),

    # 课程表 course
    path('admin/<int:name>/course_list/', admin.course_list),
    path('admin/<int:name>/course_add/', admin.course_add),
    path('admin/<int:name>/course_editor/', admin.course_editor),
    path('admin/<int:name>/course_delete/', admin.course_delete),

    # 授课表
    path('admin/<int:name>/teaching_list/', admin.teaching_list),
    path('admin/<int:name>/teaching_add/', admin.teaching_add),
    path('admin/<int:name>/teaching_delete/', admin.teaching_delete),
    path('admin/<int:name>/teaching_editor/', admin.teaching_editor),

    # 班级课程表
    path('admin/<int:name>/class_course_list/', admin.class_course_list),
    path('admin/<int:name>/class_course_add/', admin.class_course_add),
    path('admin/<int:name>/class_course_editor/', admin.class_course_editor),
    path('admin/<int:name>/class_course_delete/', admin.class_course_delete),

    # 搜索
    path("admin/<int:name>/search/", admin.search),

    path('admin/<int:name>/admin/', admin.admin),  # 个人信息显示
    path('admin/<int:name>/admin_pwd/', admin.admin_pwd),


    # 学生
    path('student/<int:name>/student_list/', student.student_list),
    path('student/<int:name>/course/', student.course),
    path('student/<int:name>/choose/', student.choose),
    path('student/<int:name>/pwd/', student.pwd),

    ## 教师
    path('teacher/<int:name>/teacher_list/', teacher.teacher_list),
    path('teacher/<int:name>/teacher_electives/', teacher.teacher_electives),
    path('teacher/<int:name>/teacher_registration/', teacher.registration),
    path('teacher/<int:name>/teacher_pwd/', teacher.teacher_pwd),
]
