from django.urls import path , re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('' , views.signup_view, name='home'),
    re_path(r'^signup/$' , views.signup_view, name='signup')
]