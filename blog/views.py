from django.views import generic
from .models import Post, Event
from django.shortcuts import render, redirect, reverse, get_object_or_404

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    event_category = Event.objects.filter()
    template_name = 'event_list.html'

def all_events(request):
    """ A view to show all events, possibly filtered by category """

    events = Event.objects.all()
    query = None
    category = None
    direction = None

    if request.GET:      
        if 'category' in request.GET:
            category = request.GET['category']
            events = events.filter(event_category=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('events'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            events = events.filter(queries)

    context = {
        'events': events,
        'search_term': query,
        'category': category,
    }

    return render(request, 'blog/event_list.html', context)









def post_detail(request, post_slug):
    """ A view to show blog post detail page """

    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)
