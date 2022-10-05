from django.contrib import admin

# Register your models here.

from .models import Chirp

admin.site.register(Chirp)