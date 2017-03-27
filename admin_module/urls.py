from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
   url(r'^index/$',views.post_home),
    #admin_module/event/add
    url(r'^event/add/$',views.createEvent.as_view(),name='event-add'),
]
