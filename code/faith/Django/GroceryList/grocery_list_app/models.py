from django.db import models
import datetime
from django.utils import timezone



class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    completed_date = models.DateTimeField('date completed', blank=True, null=True)
    completed = models.BooleanField('completed', default=False)
    def __str__(self):
        return self.text_description



