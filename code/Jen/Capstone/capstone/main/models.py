
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RabbitModel(models.Model):
    caption = models.TextField(max_length=255)
    photo = models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.caption + ": " + str(self.photo)


class ResidentFront(models.Model):
    caption = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='uploads/')
    information: models.TextField(max_length=500)


class ResidentBack(models.Model):
    parents=models.TextField(max_length=100)
    age=models.CharField(max_length=20)
    showWins=models.CharField(max_length=200)
    ancestorInfo=models.TextField(max_length=300)

