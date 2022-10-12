from django.contrib import admin
from .models import RabbitModel, ResidentBack, ResidentFront

admin.site.register(RabbitModel)
admin.site.register(ResidentFront)
admin.site.register(ResidentBack)

# Register your models here.
