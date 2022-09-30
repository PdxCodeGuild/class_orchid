from django.db import models


class UrlShort(models.Model):
    long_url = models.TextField()
    short_url = models.TextField(max_length=100)
    
    def __str__(self):
        return self.short_url
# Create your models here.
