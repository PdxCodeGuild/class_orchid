from django.db import models


class GroceryItem(models.Model):
    grocery_item_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
