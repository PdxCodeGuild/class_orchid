from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chirp(models.Model):
    content = models.CharField(max_length=285)
    posted_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)