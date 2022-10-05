from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class WordDef(models.Model):
    new_word = models.CharField(max_length=50)
    datetime_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.new_word