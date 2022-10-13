from django.db import models
from django.contrib.auth.models import AbstractUser
from exercise.models import Exercise

DAYS = (
    ('mon','Monday'),
    ('tues', 'Tues')
)

class CustomUser(AbstractUser):
    age = models.CharField(max_length=3, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    # workout = models.ManyToManyField(Exercise, through = 'UserWorkout', through_fields = ('user', 'exercise'))
    
# class UserWorkout(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#     day = models.CharField(max_length=20, choices=DAYS)
#     reps = ...
#     weight = ...
#     note = ...