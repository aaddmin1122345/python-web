# Generated by Django 4.1.2 on 2022-12-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_courses_course_choose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.SmallIntegerField(choices=[(1, '开放选课'), (2, '关闭选课')], verbose_name='是否开放选课')),
            ],
        ),
    ]
