from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Log(models.Model):
    logrun_post = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    auth_users = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="logrun_post")
    access_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.Log
