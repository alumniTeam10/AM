from django.contrib import admin
from .models import User,Student,Alumni,Faculty

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Alumni)
admin.site.register(Faculty)