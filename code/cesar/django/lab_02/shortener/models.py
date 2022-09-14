from django.db import models

# Create your models here.


class UrlShortener(models.Model):
    long_url = models.CharField(
        max_length=300, default="https://www.google.com")
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return self.long_url
