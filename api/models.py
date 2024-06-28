from django.db import models


# Create your models here.
# 超级管理员表:ID,密码
class Root(models.Model):
    id = models.AutoField(verbose_name='超级管理员', primary_key=True)  # (主键)
    password = models.CharField(verbose_name='密码', max_length=64)


# 院系表：院系ID，院系名称
class Departments(models.Model):
    departments = models.AutoField(verbose_name='院系', primary_key=True)   #(主键)
    departments_name = models.CharField(verbose_name='院系名称', max_length=(64))
    def __str__(self):
        return self.departments_name


# 管理员表：ID，姓名，院系
class Administrator(models.Model):
    administrator = models.AutoField(verbose_name="管理员", primary_key=True)  # (主键)
    administrator_name = models.CharField(verbose_name="姓名", max_length=64)
    administrator_departments = models.ForeignKey(verbose_name='院系', to='Departments', to_field='departments', on_delete=models.CASCADE)     # (外键)
    password = models.CharField(max_length=255, null=True)
    mail = models.EmailField(verbose_name="邮箱", null=True)


# 教师表：职工号，院系，姓名，性别，出生年月，联系电话
class Teacher(models.Model):
    teacher = models.IntegerField(verbose_name="职工号", primary_key=True, )    # (主键)
    teacher_departments = models.ForeignKey(verbose_name='院系', to='Departments', to_field='departments', on_delete=models.CASCADE)     # (外键)
    teacher_name = models.CharField(verbose_name="姓名", max_length=64)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    teacher_gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    teacher_time = models.DateField(verbose_name="出生年月", )
    teacher_phone = models.IntegerField(verbose_name="联系电话", max_length=64)
    password = models.CharField(max_length=255, null=True)
    mail = models.EmailField(verbose_name="邮箱", null=True)
    def __str__(self):
        return self.teacher_name


# 专业表：专业ID，专业名称,院系
class Professional(models.Model):
    professional = models.AutoField(verbose_name="专业ID", primary_key=True)      # (主键)
    professional_name = models.CharField(verbose_name="专业名称", max_length=255)
    administrator_departments = models.ForeignKey(verbose_name='院系', to='Departments', to_field='departments', default=1001, on_delete=models.CASCADE)

    def __str__(self):
        return self.professional_name


# 课程表：课程编号，课程名称，学分，院系
class Courses(models.Model):
    course = models.AutoField(verbose_name="课程编号", primary_key=True)      # (主键)
    course_name = models.CharField(verbose_name="课程名称", max_length=255)
    course_credits = models.IntegerField(verbose_name="学分", )
    course_departments = models.ForeignKey(verbose_name='院系', to='Departments', to_field='departments', default=1001, on_delete=models.CASCADE)
    course_choices = (
        (1, "选修"),
        (2, "必修"),
    )
    course_choose = models.SmallIntegerField(verbose_name="选修/必修", choices=course_choices)
    def __str__(self):
        return self.course_name


# 班级表：班级ID，班级名称,专业ID
class Class(models.Model):
    classID = models.AutoField(verbose_name="班级ID", primary_key=True)      # (主键)
    class_name = models.CharField(verbose_name="班级名称", max_length=255)
    professional = models.ForeignKey(verbose_name='专业', to='Professional', to_field='professional', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name


# 学生表：学号，姓名，性别，出生年月，系名，专业,班级
class Students(models.Model):
    student = models.IntegerField(verbose_name="学号", primary_key=True)      # (主键)
    student_name  = models.CharField(verbose_name="姓名", max_length=32)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    student_gender  = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    student_time  = models.DateField(verbose_name="出生年月", )
    student_class = models.ForeignKey(verbose_name="班级", to="Class", to_field="classID", default=1, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, null=True)
    mail = models.EmailField(verbose_name="邮箱", null=True)


# 授课表：职工号(外键)(级联删除)，课程编号(外键)(级联删除)
class Teaching(models.Model):
    course = models.ForeignKey(verbose_name='课程', to='Courses', to_field='course', on_delete=models.CASCADE)
    teacher = models.ForeignKey(verbose_name='教师', to='Teacher', to_field='teacher', on_delete=models.CASCADE)


# 班级课程
class Class_course(models.Model):
    course = models.ForeignKey(verbose_name='课程', to='Courses', to_field='course', on_delete=models.CASCADE)
    classid = models.ForeignKey(verbose_name='班级', to='Class', to_field='classID', on_delete=models.CASCADE)


# 选修表：学号，课程编号，成绩
class Electives(models.Model):
    electives = models.AutoField(verbose_name="选修ID", primary_key=True, )
    student = models.ForeignKey(verbose_name='学号', to='Students', to_field='student', on_delete=models.CASCADE)    # (外键)
    course = models.ForeignKey(verbose_name='课程编号', to='Courses', to_field='course', on_delete=models.CASCADE)   # (外键)
    course_results = models.IntegerField(verbose_name="成绩", max_length=12, default=0)

# 选课开放
class Course_selection(models.Model):
    choices = (
        (1, "开放选课"),
        (2, "关闭选课"),
    )
    course = models.SmallIntegerField(verbose_name="是否开放选课", choices=choices, default=2)