from django.db import models

# Create your models here.

# I will need a model (place to store) to store a long url and short code
# in views i will import from models

class ShortLink(models.Model):
    short_code = models.CharField(max_length=6)
    long_url = models.CharField(max_length=500)