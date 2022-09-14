from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Chirp(models.Model):
    content = models.CharField(max_length=300)
    posted_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


