from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

from api import models

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0.排除那些不需要登录就能访问的页面
        #   request.path_info 获取当前用户请求的URL /login/
        url = request.path_info
        if url == "/login/" or url == "/root_login/" or url == "/img/code/" or url == "/con_pwd/" or url == "/email/" or url == "/logout/"or url == "/sql/":
            return
        # 1.读取当前访问的用户的session信息，如果能读到，说明已登陆过，就可以继续向后走。
        dict = request.session.get("info")
        if dict:
            id = dict["id"]
            root_id = models.Root.objects.filter(id=id).first()
            student_id = models.Students.objects.filter(student=id).first()
            teacher_id = models.Teacher.objects.filter(teacher=id).first()
            admin_id = models.Administrator.objects.filter(administrator=id).first()
            if root_id != None:
                if url[0:5] == "/root":
                    return
                else:
                    return redirect("/root_login/")
            elif student_id != None:
                if url[0:8] == "/student" and url[9:19] == str(id):
                    return
                else:
                    return redirect("/login/")
            elif teacher_id != None:
                if url[0:8] == "/teacher":
                    return
                else:
                    return redirect("/login/")
            elif admin_id != None:
                departments = models.Departments.objects.filter(administrator__administrator=id).values("departments").first()
                if url[0:6] == "/admin" and url[7:11] == str(departments["departments"]):
                    return
                else:
                    return redirect("/login/")
            else:
                return redirect("/login/")
        else:
            return redirect("/login/")
