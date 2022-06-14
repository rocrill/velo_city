from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('posts/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('events/', views.all_events, name='events'),
]
