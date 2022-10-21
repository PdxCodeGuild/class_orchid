from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    new_post = models.CharField(max_length=500)
    datetime_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    def __str__(self):
        return self.new_post
# Create your models here.
