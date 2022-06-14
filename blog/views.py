from django.views import generic
from .models import Post, Event

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'event_list.html'