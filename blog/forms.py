from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Event
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    event_date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'