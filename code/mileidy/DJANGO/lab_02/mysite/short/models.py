from django.db import models

class Short(models.Model):
    long_url = models.CharField(max_length=300)
    short_code = models.CharField(max_length=6)