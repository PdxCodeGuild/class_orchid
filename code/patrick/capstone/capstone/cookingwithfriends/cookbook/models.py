from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    recipetitle = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=250)
    recipelines = models.CharField(max_length=2500)
    #pricefilter = models.Choices[
     #   ('one','$'),
      #  ('two','$$'),
       # ('three','$$$'),
    #]
    date_posted = models.DateTimeField(default= timezone.now)
    ruser = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})



