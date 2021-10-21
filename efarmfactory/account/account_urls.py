from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import registerView,activateAccount,profile,demo
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('register/', registerView.as_view(),name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    path('activate<uidb64>/<token>', activateAccount.as_view(),name='activate'),
    path('profile/',profile,name='profile'),
    path('demo/',demo,name='demo')
]
