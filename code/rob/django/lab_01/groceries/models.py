from datetime import datetime
import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField(null = True, blank = True)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.text_description

    def was_created_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)