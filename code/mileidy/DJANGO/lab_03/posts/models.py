from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    chirp_text = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # foreign key

    def __str__(self):
        return self.chirp_text
