from django.contrib import admin
from django.urls import path
from . import views 

#this is a test line
#this is test line 2

urlpatterns = [
    path('', views.article_list),
]
