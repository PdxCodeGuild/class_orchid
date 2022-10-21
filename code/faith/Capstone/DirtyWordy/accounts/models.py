from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Fav(models.Model):
    favList = models.CharField(max_length=500)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    wordlist = models.CharField(max_length=500)
    def __str__(self):
        return self.favList
    