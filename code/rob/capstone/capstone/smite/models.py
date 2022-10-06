from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Skin(models.Model):
    god_icon_url = models.URLField()
    god_skin_url = models.URLField()
    god_name = models.CharField(max_length=30)
    god_id = models.IntegerField()

    def __str__(self):
        return_str = self.god_name + self.god_skin_url
        return return_str

class Session(models.Model):
    getter_id = models.IntegerField()
    session_id = models.CharField(max_length=100)

    def __str__(self):
        return self.session_id