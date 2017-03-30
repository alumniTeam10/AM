from django import forms
from django.core import validators
from  Database.models import  Event
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

