# core/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Message(models.Model):
    VISIBILITY_CHOICES = [('public', 'Public'), ('private', 'Private')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    unlock_datetime = models.DateTimeField()
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')
    
    # optional media
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    # Additional fields
    mood = models.CharField(max_length=50, blank=True)  # For sentiment filter
    is_nsfw = models.BooleanField(default=False)
    is_malicious = models.BooleanField(default=False)

    def is_unlocked(self):
        return timezone.now() >= self.unlock_datetime

    def __str__(self):
        return self.heading
