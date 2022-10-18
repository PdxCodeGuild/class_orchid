from cgi import print_exception
from time import timezone
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=10)
    departing = models.CharField(max_length=4)
    arriving = models.CharField(max_length=4)

    def __str__(self):
        return self.user.username
        # , self.price, self.departing, self.arriving

# class Comment(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     time_created = models.DateTimeField(default=timezone.now)
#     text = models.CharField(max_length=200)



