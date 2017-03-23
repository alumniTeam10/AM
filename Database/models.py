from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number=models.CharField(max_length=12)
    secret_question=models.CharField(max_length=100)
    secret_question_answer=models.CharField(max_length=150)
    create_date=models.DateField(null=True)
    update_date=models.DateField(null=True)
    user_type_flag=models.CharField(max_length=10)


class Student(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    department_name=models.CharField(max_length=50)
    branch_name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=40)
    admission_date=models.DateField()
    create_date = models.DateField()
    update_date = models.DateField()
    active_flag=models.BooleanField()


class Alumni(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    department_name=models.CharField(max_length=50)
    branch_name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=40)
    admission_date=models.DateField()
    passout_date = models.DateField()
    current_organization_name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    work_phone=models.CharField(max_length=12)
    create_date = models.DateField()
    update_date = models.DateField()
    active_flag=models.BooleanField()


class Faculty(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    department_name=models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    create_date = models.DateField()
    update_date = models.DateField()
    active_flag=models.BooleanField()

