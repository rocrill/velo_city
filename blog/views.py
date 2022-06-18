from datetime import date
from django.views import generic
from .models import Post, Event
from .forms import PostForm, EventForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator


def all_posts(request):
    """View to show list of blog posts, in order of most recently created."""
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')

    context = {
        'post_list': paginator.get_page(page),
    }

    return render(request, 'blog/post_list.html', context)


def all_events(request):
    """ A view to show all events, filtered by event date, with option to filter by category."""
    events = Event.objects.all()
    events = events.filter(event_date__gte=date.today())
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
    """ Add a blog post to the blog section of the website."""
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
            try:
                form.save()
                messages.success(request,
                                "Success!" +
                                " Your event has been" +
                                " added.")
            except ValidationError as e:
                messages.error(request, e.message)

    form = EventForm()
        
    template = 'blog/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit an event post. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Successfully updated event!')
                return redirect(reverse('events'))
            except ValidationError as e:
                messages.error(request, e.message)
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    template = 'blog/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_slug):
    """ Edit a blog post."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=post_slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_slug):
    """ Delete a blog post from the website."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_slug)
    post.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('post_list'))


@login_required
def delete_event(request, event_id):
    """ Delete an event post from the website"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))