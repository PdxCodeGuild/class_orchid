

from django.db import models
from django.contrib.auth.models import User




class Input(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_chirp = models.CharField(max_length=128)
    
    def __str__(self):
        return self.new_chirp
   