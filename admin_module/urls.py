from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
   url(r'^index/$',views.post_event),
    url(r'^news/$',views.post_news),
    #admin_module/event/add
    url(r'^event/add/$',views.createEvent,name='event-add'),
    url(r'^eventForm/',views.form_name_view,name='form_name'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='deleteEvent'),
]
