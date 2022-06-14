from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('events/', views.EventList.as_view(), name='events'),
]
