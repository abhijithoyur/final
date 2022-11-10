from django.urls import path
from django.shortcuts import render, redirect
from .import views
app_name='school'
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name="login"),
    path('form',views.form,name="form"),
    path('registration',views.registration,name="registration"),
    path('finalform',views.finalform,name='finalform'),
    path("submiting",views.submiting,name="submiting")
]
