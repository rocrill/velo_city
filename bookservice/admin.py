from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
     """This class defines admin page for the Booking model."""
    readonly_fields = ('date',
                       )
    fields = ('first_name', 'last_name', 'service_type',)

    list_display = ('first_name', 'last_name', 'date', 'service_type')

    ordering = ('-date',)

admin.site.register(Booking, BookingAdmin)