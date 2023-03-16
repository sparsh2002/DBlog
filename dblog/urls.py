from django.contrib import admin
from django.urls import path , include
from . import views 

#this is a test line
#this is test line 2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/' , include('articles.urls')),
    path('about/', views.about ),
    path('', views.homepage ),
]
