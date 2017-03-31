from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import Http404
from sympy.functions.elementary.complexes import re
from django.contrib.auth.decorators import login_required
from django.utils.decorators import  method_decorator
from django.urls import reverse_lazy
from Database.models import Event,User,Student
from  admin_module.forms import EventForm,UserForm
from django.shortcuts import redirect
from AlumniManagement import settings
from django.forms import inlineformset_factory
# Create your views here.
class EventDelete(DeleteView):
    model=Event
    success_url = reverse_lazy("view-event")

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


def createUser(request):
    form=UserForm()
    if request.method =='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return viewUsers(request)
    return render(request,'AlumniManagement/user_formpage.html',{'form':form})


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy("view-event")

def viewEvent(request,pk):

    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL, request.path)

    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        raise Http404("The Event you are searching for does not exists")

    return render(
        request,
        'AlumniManagement/viewEvent.html'

    )


class EventUpdate(UpdateView):
    news_event_flag = False
    model = Event
    fields = ['event_name','event_info']
    template_name_suffix = '_update_form'


    def get_success_url(self):
        obj = super(EventUpdate,self).get_object(

        )
        if obj.event_news_flag==True:
            print obj.event_info
            success_url=reverse_lazy("view-event")
        else:
            success_url = reverse_lazy("view-news")
        return success_url

class UserUpdate(UpdateView):
    model = User
    #fields = __all__
    form_class = UserForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("view-users")


def viewUsers(request):
    user_list=User.objects.all()
    userList=[]

    for user in user_list:
        userList.append(user)
        user_dict={'user_name':userList}
    return render(request,'AlumniManagement/viewUsers.html',context=user_dict)





def manageUser(request,id):
    user=User.objects.get(pk=id)
    UserformSet=inlineformset_factory(User,Student,fields=('department_name','branch_name',))
    if request.method=="POST":
        formset=UserformSet(request.POST,request.FILES,instance=user)
        if formset.is_valid():
            formset.save()
            success_url = reverse_lazy("view-users")
            return success_url
    else:
           formset=UserformSet(instance=user)

    return render(request,'AlumniManagement/user_update.html',{'formset':formset})