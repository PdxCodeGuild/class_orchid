from django.db import models

# Create your models here.

class ShortURL(models.Model):
    long_url = models.CharField('long_url', max_length=2048)
    short_url = models.CharField('short_url', max_length=24)