from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^(student|faculty|alumni)/$', views.UserDocuments,name='UserDocuments'),
    #url(r'^alumni/$', views.alumni,name='alumni'),
    # url(r'^alumni/search/$', views.search_alumni, name='search_alumni'),
    #url(r'^faculty/$', views.faculty,name='faculty'),
    # url(r'^faculty/search/$', views.search_faculty, name='search_faculty'),
]