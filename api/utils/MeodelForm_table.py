from django import forms
from django.shortcuts import render, redirect

from itertools import chain

from api import models
from api.utils.bootstrap import BootStrapModelForm,BootStrapForm


# ModelForm添加院系数据
class MyForm_Departments(BootStrapModelForm, forms.ModelForm):
    class Meta:
        model = models.Departments
        fields = ['departments_name']


# ModelForm添加专业数据
class MyForm_Professional(BootStrapModelForm, forms.ModelForm):
    class Meta:
        model = models.Professional
        fields = ['professional_name', 'administrator_departments']


# ModelForm添加班级数据
class MyForm_Class(BootStrapModelForm, forms.ModelForm):
    class Meta:
        model = models.Class
        fields = ['class_name', 'professional']


# ModelForm添加教师数据
class MyForm_Teacher(BootStrapModelForm, forms.ModelForm):

    class Meta:
        model = models.Teacher
        fields = ['teacher_departments', 'teacher_name', 'teacher_gender', 'teacher_time', 'teacher_phone', 'mail']


# ModelForm添加学生数据
class MyForm_Student(BootStrapModelForm, forms.ModelForm):
    class Meta:
        model = models.Students
        fields = ['student_name', 'student_gender', 'student_time', 'student_class', 'mail']


# Modelorm添加课程信息
class MyForm_Courses(BootStrapModelForm, forms.ModelForm):
    class Meta:
        model = models.Courses
        fields = ['course_name', 'course_credits', 'course_departments', 'course_choose']


# 添加院系管理员
class MyForm_Administrator(BootStrapModelForm, forms.ModelForm):
    class Meta:
        model = models.Administrator
        fields = ['administrator_name', 'administrator_departments', 'mail']

# class MyForm_Administrator_Login(BootStrapModelForm, forms.ModelForm):
#     class Meta:
#         model = models.Administrator_Login
#         fields = []

class MyForm_Root(BootStrapModelForm):
    class Meta:
        model = models.Root
        fields = []


class PWDeditor(BootStrapForm):
    password = forms.CharField(
        label="原密码",
        widget=forms.PasswordInput,
        required=True,
    )
    new_password = forms.CharField(
        label="新密码",
        widget=forms.PasswordInput,
        required=True,
    )
    con_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput,
        required=True
    )


# 授课
class MyForm_Teaching(BootStrapModelForm):
    class Meta:
        model = models.Teaching
        fields = ["teacher", "course"]


# 班级课程
class MyForm_Class_course(BootStrapModelForm):
    class Meta:
        model = models.Class_course
        fields = ["classid", "course"]


class MyForm_Electives(BootStrapModelForm):
    class Meta:
        model = models.Electives
        fields = ["course_results"]


class MyForm_Course_selection(BootStrapModelForm):
    class Meta:
        model = models.Course_selection
        fields = ["course"]


class MyForm_chooce(BootStrapForm):
 class Meta:
     model = models.Electives
     filter = []