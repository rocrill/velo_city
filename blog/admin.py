"""Defines models for admin page."""

from django.contrib import admin
from .models import Post, Event


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """This class defines admin page for the Post model."""
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on', 'image')
    search_fields = ('title', 'content')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """This class defines admin page for the Event model."""
    prepopulated_fields = {}
    list_filter = ('status', 'created_on')
    list_display = (
        'title',
        'status',
        'created_on',
        'image',
        'event_category',
        'event_date')
    search_fields = ('title', 'content')
