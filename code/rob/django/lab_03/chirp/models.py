from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Chirp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=128)


class Like(models.Model):
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=128)


class Rechirp(models.Model):
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
