from django.db import models

# Create your models here.

# null and blank is a way of telling django im ok with blank dates

class GroceryItem(models.Model):
    item_name = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField(
        'date completed', null=True, blank=True)
    completed = models.BooleanField(default=False)
