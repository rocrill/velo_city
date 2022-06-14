from django.views import generic
from .models import Post, Event
from django.shortcuts import render, redirect, reverse, get_object_or_404

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'event_list.html'

def post_detail(request, post_slug):
    """ A view to show blog post detail page """

    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)
