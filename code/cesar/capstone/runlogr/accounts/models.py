from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Token(models.Model):

    refresh_token = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.refresh_token == None:
            return "ERROR: TOKEN IS NULL"
        return self.refresh_token

# class New_Post(models.Model):
#     type = models.CharField(max_length=100, null=True)
#     distance = models.CharField(max_length=100, null=True)
#     time = models.CharField(max_length=100, null=True)
#     name = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         if self.name == None:
#             return "ERROR: VALUE IS NULL"
#         return self.name

