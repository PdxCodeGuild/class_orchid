import datetime
from xmlrpc.client import boolean

from django.db import models
from django.utils import timezone

# Create your models here.

class GroceryList(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='Add Description')
    pub_date = models.DateTimeField(auto_now_add=True)
    comp_date = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)