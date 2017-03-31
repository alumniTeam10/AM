from django import forms
from django.core import validators
from  Database.models import  Event,User,Student,Faculty,Alumni
from django.forms.models import inlineformset_factory
class EventForm(forms.ModelForm):
    class Meta():
        model=Event
        fields='__all__'
    '''event_name = forms.CharField()
    event_info= forms.CharField(widget=forms.Textarea)
    expiration_date=forms.DateField()
    createdBy=forms.CharField()
    event_news_flag=forms.BooleanField()
    created_date=forms.DateField()
    updated_date=forms.DateField()
    active_flag=forms.BooleanField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])'''


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','phone_number','user_type_flag']


'''from Database.models import (
User,
Alumni,
Student,
Faculty
)

UserFormSet=inlineformset_factory(
    User,
    Student,fields=('department_name','branch_name','course_name','admission_date','create_date',
                    'update_date','active_flag',)


)'''
