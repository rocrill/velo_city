from django.shortcuts import render
from .forms import BookingForm
from .models import Booking
from profiles.models import UserProfile
from django.contrib import messages

# Create your views here.

def bookservice(request):
    """ View to return to the bookservice page. """
    if request.method=="POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'date': request.POST['date'],
            'service_type': request.POST['service_type'],
            'bike_type': request.POST['bike_type'],
            
        }
        form = BookingForm(form_data)
        if form.is_valid():
            form.save()
            messages.success(request,
                            "Thanks for submitting your service booking!" +
                            " We will be in touch to confirm your" +
                            " booking slot.")

    booking_form = BookingForm()
    context = {
        'booking_form': booking_form,
    }
    return render(request, 'bookservice/bookservice.html', context)

