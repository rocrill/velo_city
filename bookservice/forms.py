from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
     """Form for the booking model."""
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'phone_number', 'email_address', 'date', 'service_type',)

    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)

       