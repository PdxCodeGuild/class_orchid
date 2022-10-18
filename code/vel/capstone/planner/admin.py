from django.contrib import admin

from .models import WorkingSet, Workout


admin.site.register(Workout)
admin.site.register(WorkingSet)

# Register your models here.
