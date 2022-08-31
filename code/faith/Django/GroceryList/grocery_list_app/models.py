from django.db import models
import datetime
from django.utils import timezone



class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField('date completed')
    completed = models.BooleanField('completed')
    def __str__(self):
        return self.text_description



