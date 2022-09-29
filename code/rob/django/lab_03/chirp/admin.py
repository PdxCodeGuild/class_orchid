from django.contrib import admin
from .models import Chirp, Like, Comment, Rechirp

# Register your models here.
admin.site.register(Chirp)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Rechirp)