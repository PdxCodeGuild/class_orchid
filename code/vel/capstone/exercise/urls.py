from django.urls import path, include
from . import views

app_name = 'exercise'
urlpatterns = [
    path('', views.index, name="index"),
]