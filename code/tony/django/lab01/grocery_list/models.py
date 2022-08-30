from django.db import models

class GroceryItem(models.Model):
    description = models.CharField('item description', max_length=4096)
    creation_date = models.DateTimeField('creation date')
    completion_date = models.DateTimeField('completion date', null=True)
    is_complete = models.BinaryField('complete')
