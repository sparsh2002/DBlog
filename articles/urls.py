from django.contrib import admin
from django.urls import path , re_path
from . import views 

#this is a test line
#this is test line 2

app_name = 'articles'

urlpatterns = [
    path('', views.article_list , name="list"),
    path('create' , views.article_create , name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$' , views.article_detail , name="detail")
]


