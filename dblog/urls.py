from django.contrib import admin
from django.urls import path , include
from . import views 
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
#this is a test line
#this is test line 2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/' , include('articles.urls')),
    path('about/', views.about ),
    path('', views.homepage ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += staticfiles_urlpatterns()