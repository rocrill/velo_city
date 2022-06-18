from django.db import models
import datetime
from django.core.exceptions import ValidationError

class Booking (models.Model):
    """Model for service bookings."""
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    email_address = models.CharField(max_length=60, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField(default=datetime.date.today())
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

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Booking, self).save(*args, **kwargs)

