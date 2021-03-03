from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_reroute),
    path('login', views.login),
    path('create_user', views.register),
    path('log_in', views.log_in),
    path('sucess', views.sucess),
]