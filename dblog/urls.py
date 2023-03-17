from django.contrib import admin
from django.urls import path , include
from . import views 
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
#this is a test line
#this is test line 2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/' , include('articles.urls')),
    path('accounts/' , include('accounts.urls')),
    path('about/', views.about ),
    path('', article_views.article_list , name='home' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT )

# urlpatterns += staticfiles_urlpatterns()