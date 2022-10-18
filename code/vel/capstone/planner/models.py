from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.forms import CharField

class Planner(models.Model):
    title = models.CharField(max_length = 200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE, related_name='user_planner')
