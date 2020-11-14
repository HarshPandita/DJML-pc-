
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin

from . import views

urlpatterns = [
    path('',views.home),
    path('question/',views.question,name='question'),
    path('dash/',views.dash,name='home'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

]
