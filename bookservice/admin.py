from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ('date',
                       )

    fields = ('first_name', 'last_name', 'service_type',
                  'bike_type',)

    list_display = ('first_name', 'last_name', 'date', 'service_type',
                  'bike_type')

    ordering = ('-date',)

admin.site.register(Booking, BookingAdmin)