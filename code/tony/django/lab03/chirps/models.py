from datetime import datetime
from django.db import models
from django.conf import settings

class Chirp(models.Model):
    chirp = models.CharField(max_length=140)
    authuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
