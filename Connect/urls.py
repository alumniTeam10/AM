from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^(student|faculty|alumni)/$', views.connect,name='connect'),
    url(r'^(student|faculty|alumni)/search/$', views.search, name='search'),

    url(r'^(student|faculty|alumni)/view/$', views.view, name='view'),
    #url(r'^alumni/$', views.alumni,name='alumni'),
    # url(r'^alumni/search/$', views.search_alumni, name='search_alumni'),

    #url(r'^faculty/$', views.faculty,name='faculty'),
    # url(r'^faculty/search/$', views.search_faculty, name='search_faculty'),
]