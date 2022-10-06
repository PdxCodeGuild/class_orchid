from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    recipetitle = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=250)
    recipelines = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    ruser = models.ForeignKey(User, on_delete=models.CASCADE)
    pricechoices = [
        ('one','$'),
        ('two','$$'),
        ('three','$$$'),
    ]
    pricefilter = models.CharField(choices = pricechoices, max_length=5, default='two')

    def __str__(self):
        return (self.recipetitle)


    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})



