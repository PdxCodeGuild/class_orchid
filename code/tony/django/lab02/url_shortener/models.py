from django.db import models
from django.urls import reverse


class Url(models.Model):
    longurl = models.CharField('long url', max_length=2048, unique=True)
    shortcode = models.CharField('shortcode', max_length=16, unique=True)
