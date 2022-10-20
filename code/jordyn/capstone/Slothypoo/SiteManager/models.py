from datetime import datetime
from email.policy import default
from random import choices
from django.db import models

TAG_CHOICES = (
    ('select tag', 'Select Tag'),
    ('colored', 'Colored'),
    ('emote', 'Emote'),
    ('bust', 'Bust'),
    ('half-Body', 'Half-body'),
    ('full-Body', 'Full-body'),
)

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    tags = models.CharField(max_length=15, choices = TAG_CHOICES, default = 'Select Tag')
    add_date = models.DateTimeField(auto_now_add=True)
    is_NSFW = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    