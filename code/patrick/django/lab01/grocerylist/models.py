from django.db import models
import datetime
from django.utils import timezone
class GroceryItem(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    #complete_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    