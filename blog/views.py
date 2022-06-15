from django.views import generic
from .models import Post, Event
from .forms import PostForm, EventForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

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
    events = events.order_by('event_date')
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

@login_required
def add_post(request):
    """ Add a blog post to the blog section of the website"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def add_event(request):
    """ Add an event to the events section of the website"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('event_list'))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'blog/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
