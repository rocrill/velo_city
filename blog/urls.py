from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('posts/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('posts/add', views.add_post, name='add_post'),
    path('events/', views.all_events, name='events'),
    path('events/add/', views.add_event, name='add_event'),
]
