from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='post_list'),
    path('posts/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('posts/add', views.add_post, name='add_post'),
    path('edit/<slug:post_slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:post_slug>/', views.delete_post, name='delete_post'),

    path('events/', views.all_events, name='events'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
