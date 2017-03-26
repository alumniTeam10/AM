from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
     url(r'^$', views.UserDocuments,name='UserDocuments'),
    #url(r'^(?P<document_id>[0-9]+)/$', views.UserDocuments,name='UserDocuments'),
    #url(r'^alumni/$', views.alumni,name='alumni'),
    # url(r'^alumni/search/$', views.search_alumni, name='search_alumni'),
    #url(r'^faculty/$', views.faculty,name='faculty'),
    # url(r'^faculty/search/$', views.search_faculty, name='search_faculty'),
]