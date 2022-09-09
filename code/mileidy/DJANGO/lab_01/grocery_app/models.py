from django.db import models

class Groceryitem(models.Model):
    text_description = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add = True)
    date_completed = models.DateTimeField(blank = True, null = True )
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.text_description