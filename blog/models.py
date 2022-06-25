from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    """Model for blog posts."""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Event(models.Model):
    """Model for event posts."""
    title = models.CharField(max_length=200, unique=True)
    event_category = models.CharField(max_length=200, unique=True)
    event_date = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=False, blank=False)

    CATEGORY_TYPES = [
            ('Ladies cycling', 'Ladies cycling'),
            ('Mens cycling', 'Mens cycling'),
            ('Racing', 'Racing'),
            ('Social', 'Social'),
        ]
        
    event_category = models.CharField(
        max_length=40,
        choices=CATEGORY_TYPES,
        default='Racing',
    )

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.event_date.date() < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Event, self).save(*args, **kwargs)


