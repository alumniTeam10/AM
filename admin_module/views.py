from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from sympy.functions.elementary.complexes import re
from django.contrib.auth.decorators import login_required
from django.utils.decorators import  method_decorator
from django.urls import reverse_lazy
from Database.models import Event
from  admin_module.forms import EventForm

# Create your views here.

def post_event(request):
    event_list=Event.objects.all()
    eventsList=[]

    for eve in event_list:
        if eve.event_news_flag==True:
            print eve.event_name
            #event_dict={'event_name':event_list}
            eventsList.append(eve)
        event_dict={'event_name':eventsList}
    return render(request,'AlumniManagement/viewEvent.html',context=event_dict)
    #return render(request,'web/index.html')


def post_news(request):
    news_List=Event.objects.all()
    newsList=[]
    for news in news_List:
        if news.event_news_flag==False:
            print news.event_name
            newsList.append(news)
        news_dict={'news_name':newsList}
    return render(request,'AlumniManagement/viewNews.html',context=news_dict)


def createEvent(request):
    model = Event
    fields=['event_name','event_info','createdBy','event_news_flag']
    def form_valid(self,form):
        user=self.request.user
        return super(createEvent,self).form_valid(form)
    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super(createEvent,self).dispatch(*args,**kwargs)


    #return render(request,'AlumniManagement/event_form.html')

def form_name_view(request):
    form=EventForm()

    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            if form.cleaned_data['event_news_flag']==True:
                return post_event(request)
            else:
                return post_news(request)
            #print (" event_news_flag"+form.cleaned_data['event_news_flag'])
    return render(request,'AlumniManagement/event_formpage.html',{'form':form})



class EventDelete(DeleteView):
    model=Event
    success_url = reverse_lazy('event-list')