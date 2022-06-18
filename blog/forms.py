from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Event
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    """Form for blog posts."""
    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class Event_DateTimeInput(forms.DateTimeInput):
    """Event time and date input as part of event form."""
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class EventForm(forms.ModelForm):
    """Form for event posts."""
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'image': forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput),
            'event_date': Event_DateTimeInput(format=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],),
        }

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
