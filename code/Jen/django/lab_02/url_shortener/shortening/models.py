from django.db import models



# Create your models here.

class Shortening(models.Model):
    the_url = models.CharField(max_length=500)
    shorty = models.CharField(max_length=20, default="")

 
    def __str__(self):
        return self.the_url

