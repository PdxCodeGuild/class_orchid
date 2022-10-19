from django.urls import path
from . import views 

app_name = 'planner'

urlpatterns = [
    path('add_to_workout/<str:name>/<str:desc>/', views.add_to_workout, name='add_to_workout')
]