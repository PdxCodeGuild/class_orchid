
from django.db import models



# Create your models here.



class Item(models.Model):

    grocery_item = models.CharField(max_length=100)
    checked_item = models.BooleanField(default=False)
    

    def __str__(self):
        return self.grocery_item

