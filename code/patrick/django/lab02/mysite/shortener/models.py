from django.db import models
from .gencode import gen
class Shortener(models.Model):
    longurl = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=10, default=gen) 

    def __str__(self):
        return self.longurl

