from django.conf.urls import include, url
from django.contrib import admin
from . import views



urlpatterns = [
	url(r'^$', views.index,name='index'),
	#url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^act$', views.act, name='act'),
]