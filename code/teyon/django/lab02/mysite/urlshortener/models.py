from django.db import models

class urlModel(models.Model):
    longurl = models.CharField(max_length=225)
    shorturl = models.CharField(max_length=10)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.shorturl

