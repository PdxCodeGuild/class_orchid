from django.db import models
from django.contrib.auth import get_user_model

# figure out what we want from each exercise, creating the database.

class Exercise(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    def __str__(self):
        return self.name

class Muscle(models.Model):
    name = models.CharField(max_length=500)
    muscle = models.ManyToManyField(Exercise, related_name='muscles')