from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from captcha.image import ImageCaptcha
import random,string
import gvcode   # 图片验证码库
from io import BytesIO   # 内存读取库
import random

from api import models
from api.utils.bootstrap import BootStrapModelForm,BootStrapForm
from api.utils.encrypt import md5

# Create your views here.


# 数据初始化
def sql(request):
    id = "8888"
    password = md5("root")
    models.Root.objects.create(id=id, password=password)
    return HttpResponse("重置超级管理员账户成功！")


# 后台登陆
class RootLoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True,
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

# 超级管理员登陆
def root_login(request):
    if request.method == "GET":
        form = RootLoginForm()
        return render(request, "account/root_login.html", {
            "form": form,
        })
    form = RootLoginForm(data=request.POST)
    if form.is_valid():
        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'account/root_login.html', {'form': form})
        admin_object = models.Root.objects.filter(id=form.cleaned_data["username"],
                                                      password=md5(form.cleaned_data["password"])).first()
        # admin_object = models.Students.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            # form.add_error("username", "用户名或密码错误")
            return render(request, 'account/root_login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'id': admin_object.id}
        # session可以保存1天
        # request.session.set_expiry(60 * 60 * 24 * 7)
        request.session.set_expiry(60 * 60 * 24 * 2)
        # return redirect("/root/departments_list/")
        return redirect("/root/departments_list/")
    return render(request, "account/root_login.html", {
            "form": form,
        })


# 登陆
class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True,
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    role_choices = (
        (1, "学生"),
        (2, "教师"),
        (3, "管理员")
    )
    '''单选框'''
    role = forms.ChoiceField(
        choices=role_choices,
        initial=1
    )


# 登陆
def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "account/login.html", {
            "form": form,
        })
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'account/login.html', {'form': form})

        role = form.cleaned_data["role"]
        # 学生
        if int(role) == 1:
            admin_object = models.Students.objects.filter(
                student=form.cleaned_data["username"], password=md5(form.cleaned_data["password"])).first()
            # admin_object = models.Students.objects.filter(**form.cleaned_data).first()
            if not admin_object:
                form.add_error("password", "用户名或密码错误")
                # form.add_error("username", "用户名或密码错误")
                return render(request, 'account/login.html', {'form': form})

            # 用户名和密码正确
            # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
            request.session["info"] = {'id': admin_object.student, 'name': admin_object.student_name}
            # session可以保存2天
            request.session.set_expiry(60 * 60 * 24 * 2)
            return redirect("/student/%d/student_list/"%admin_object.student)

        # 教师
        elif int(role) == 2:
            admin_object = models.Teacher.objects.filter(
                teacher=form.cleaned_data["username"], password=md5(form.cleaned_data["password"])).first()
            # admin_object = models.Students.objects.filter(**form.cleaned_data).first()
            if not admin_object:
                form.add_error("password", "用户名或密码错误")
                # form.add_error("username", "用户名或密码错误")
                return render(request, 'account/login.html', {'form': form})

            # 用户名和密码正确
            # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
            request.session["info"] = {'id': admin_object.teacher, 'name': admin_object.teacher_name}
            # session可以保存2天
            request.session.set_expiry(60 * 60 * 24 * 2)
            return redirect("/teacher/%d/teacher_list/" % admin_object.teacher)

        # 管理员
        elif int(role) == 3:
            admin_object = models.Administrator.objects.filter(
                administrator=form.cleaned_data["username"], password=md5(form.cleaned_data["password"])).first()
            if not admin_object:
                form.add_error("password", "用户名或密码错误")
                return render(request, 'account/login.html', {'form': form})
            # 用户名和密码正确
            # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
            request.session["info"] = {'id': admin_object.administrator, 'name': admin_object.administrator_name}
            # session可以保存2天
            request.session.set_expiry(60 * 60 * 24 * 2)
            name = admin_object.administrator
            name = str(name)[0:4]
            return redirect("/admin/%d/professional_list/"%int(name))
    return render(request, 'account/login.html', {'form': form})



""" 生成图片验证码 """
def image_code(request):

    # 用gvcode库生成验证码
#    img, code_string = gvcode.generate()
    # 写入到自己的session中（以便于后续获取验证码再进行校验）
#    request.session['image_code'] = code_string
    # 给Session设置60s超时
#    request.session.set_expiry(60)
#    stream = BytesIO()
#    img.save(stream, 'png')
#    return HttpResponse(stream.getvalue())
    chr_all = string.ascii_letters + string.digits
    chr_4 = ''.join(random.sample(chr_all, 4))
    image = ImageCaptcha().generate_image(chr_4)
    request.session['image_code'] = chr_4
    # 给Session设置60s超时
    request.session.set_expiry(60)
    stream = BytesIO()
    image.save(stream, 'png')
    return HttpResponse(stream.getvalue())




""" 注销 """
def logout(request):


    request.session.clear()

    return redirect('/login/')

# 找回密码
class PWDForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="新密码",
        widget=forms.PasswordInput,
        required=True,
    )
    con_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput,
        required=True,
    )
    code = forms.CharField(
        label="邮箱验证码",
        widget=forms.TextInput,
        required=True
    )


# 找回密码
def pwd_mail(request):
    if request.method == "GET":
        form = PWDForm()
        return render(request, "account/con_pwd.html", {
            "form": form,
        })
    form = PWDForm(data=request.POST)
    if form.is_valid():
        # 验证码校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('email_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'account/con_pwd.html', {'form': form})
        name = form.cleaned_data["username"]
        administrator_name = models.Administrator.objects.filter(administrator=name).first()
        student_name = models.Students.objects.filter(student=name).first()
        teacher_name = models.Teacher.objects.filter(teacher=name).first()
        password = form.cleaned_data["con_password"]
        if administrator_name != None:
            models.Administrator.objects.filter(administrator=name).update(password=md5(password))
            messages.info(request, "密码重置成功！")
            request.session.clear()
            return redirect("/login/")
        if student_name != None:
            models.Students.objects.filter(student=name).update(password=md5(password))
            messages.info(request, "密码重置成功！")
            request.session.clear()
            return redirect("/login/")
        if teacher_name != None:
            models.Teacher.objects.filter(teacher=name).update(password=md5(password))
            messages.info(request, "密码重置成功！")
            request.session.clear()
            return redirect("/login/")
    return render(request, "account/con_pwd.html", {
        "form": form,
    })




# 邮件验证码
def random_str(randomlength=4):
    str = ''
    chars = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 发送邮件验证码
def email(request):
    name = request.POST.get('username')
    email_admin = models.Administrator.objects.filter(administrator=name).values("mail").first()
    email_student = models.Students.objects.filter(student=name).values("mail").first()
    email_teacher = models.Teacher.objects.filter(teacher=name).values("mail").first()
    if email_admin != None:
        mail = email_admin["mail"]
    elif email_student != None:
        mail = email_student["mail"]
    elif email_teacher != None:
        mail = email_teacher["mail"]
    else:
        data_dict = {'msg': 404}
        return JsonResponse(data_dict)
    email_title = "xues"
    code = random_str()  # 随机生成的验证码
    request.session["email_code"] = code  # 将验证码保存到session
    email_body = "验证码为：{0}".format(code)
    sendmail = "2639709539@qq.com"
    send_mail(email_title, email_body, sendmail, [mail],)
    data_dict = {'msg': 100}
    return JsonResponse(data_dict)
