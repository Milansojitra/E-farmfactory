from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from .views import (postListView,postDetailView,postCreateView,
                    taggitListView,postUpdateView,postDeleteView,authorListView,searchView)

urlpatterns = [
    path('', postListView.as_view(),name='postlist'),
    path('create/', postCreateView.as_view(),name='postcreate'),
    path('<int:pk>/', postDetailView.as_view(),name='postdetail'),
    path('tag/<str:slug>/',taggitListView.as_view(), name='tag-list'),
    path('author/<str:username>/', authorListView.as_view(), name='authorlist'),
    path('search/<str:query>/', searchView.as_view(), name='searchview'),
    path('<int:pk>/update/', postUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', postDeleteView.as_view(), name='post-delete'),


]