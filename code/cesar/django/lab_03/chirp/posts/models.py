from django.db import models
from django.utils import timezone


# Create your models here.


class Chirps(models.Model):
    chirp = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.chirp
