from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class Booking (models.Model):
    """Model for service bookings."""
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    date = models.DateField()
    SERVICE_CHOICES = [
        ('Bike fit', 'Bike fit'),
        ('Repair', 'Repair'),
        ('Full service', 'Full service'),
    
    ]
    service_type = models.CharField(
        max_length=40,
        choices=SERVICE_CHOICES,
        default='Repair',
    )
    BIKE_CHOICES = [
        ('Hybrid', 'Hybrid'),
        ('Road', 'Road'),
    
    ]
    bike_type = models.CharField(
        max_length=15,
        choices=BIKE_CHOICES,
        default='Hybrid',
    )
