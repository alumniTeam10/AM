from django.shortcuts import render
from django.http import HttpResponse
from Database.models import Event

# Create your views here.

def post_home(request):
    event_list=Event.objects.all()
    for eve in event_list:
        print eve.event_name
    event_dict={'event_name':event_list}
    return render(request,'AlumniManagement/createEvent.html',context=event_dict)