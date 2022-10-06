from django.urls import path, include
from . import views

app_name = 'exercise'
urlpatterns = [
    path('results/', views.results, name="results"),
]