from django.db import models
from django.contrib.auth.models import AbstractUser
from exercise.models import Exercise


class CustomUser(AbstractUser):
    age = models.CharField(max_length=3, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    # workout = models.ManyToManyField(Exercise, through = 'UserWorkout', through_fields = ('user', 'exercise'))
    
