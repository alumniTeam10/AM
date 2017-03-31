from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse


class User(AbstractUser):
    phone_number=models.CharField(max_length=12, null=True, blank=True)
    secret_question=models.CharField(max_length=100, null=True, blank=True)
    secret_question_answer=models.CharField(max_length=150, null=True, blank=True)
    create_date=models.DateField(auto_now_add=True,null=True)
    update_date=models.DateField(auto_now=True,null=True)
    #profile_dp=models.FileField(null=True,blank=True)
    introduction=models.CharField(max_length=3000, null=True,blank=True)

    ADMIN='admin'
    STUDENT='student'
    ALUMNI='alumni'
    FACULTY='faculty'

    USER_TYPE_FLAG_CHOICES=(
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (ALUMNI, 'Alumni'),
        (FACULTY, 'Faculty'),
        )

    user_type_flag = models.CharField(max_length=10,choices=USER_TYPE_FLAG_CHOICES, default=ALUMNI)



    def __str__(self):
        return self.username



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

class DocumentType(models.Model):
    document_id=models.IntegerField(primary_key=True)
    document_type=models.CharField(max_length=50)
    document_info=models.TextField(editable=True)
    active_flag=models.BooleanField(default=True)

class UserDocumentMap(models.Model):
    document_type_fk=models.ForeignKey(DocumentType,primary_key=True)
    user_id=models.ForeignKey(User)
    document_info=models.TextField(editable=True)
    user_comments=models.TextField(editable=True)
    created_date=models.DateTimeField(auto_now=True)
    uploaded_date=models.DateTimeField(auto_now=True)
    active_flag = models.BooleanField(default=True)

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_info = models.TextField(editable=True)
    expiration_date = models.DateField(auto_now=True)
    createdBy = models.ForeignKey(User)
    event_news_flag = models.BooleanField()
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    active_flag = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('viewEvent',kwargs={'pk':self.pk})

    def __str__(self):
        return self.event_name


class Complaints(models.Model):
    complaint_info = models.CharField(max_length=100)
    acknowledge_flag = models.BooleanField(default=True)
    solution_info = models.TextField(editable=True)
    created_by = models.ForeignKey(User)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    active_flag = models.BooleanField(default=True)