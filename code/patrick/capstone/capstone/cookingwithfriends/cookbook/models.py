from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

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

    picture = models.ImageField( upload_to='images', blank=True, default='default2.jpg' )

    def __str__(self):
        return (self.recipetitle)


    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height  > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

