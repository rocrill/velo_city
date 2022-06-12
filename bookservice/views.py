from django.shortcuts import render

# Create your views here.

def bookservice(request):
    """ View to return to the bookservice page. """
    
    return render(request, 'bookservice/bookservice.html')