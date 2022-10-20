from django.urls import path
from . import views 

app_name = 'planner'

urlpatterns = [
    path('testing_123', views.save_workout, name='save_workout'), 
    path('add_to_workout/<str:name>/<str:desc>/', views.add_to_workout, name='add_to_workout'),
]