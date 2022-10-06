from operator import mod
from django.db import models
from django.utils import timezone

# Create your models here.
class Urls(models.Model):
    short_url = models.CharField(max_length=200)
    actual_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        str_return = f'short url: {self.short_url}, actual url: {self.actual_url}'
        return str_return

    def short_url_in_actual(self):
        actual_contains_short = self.actual_url.startswith(f'{self.short_url}')
        return actual_contains_short