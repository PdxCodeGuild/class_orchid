from django.urls import path
from . import views 

app_name = 'planner'

urlpatterns = [
    path('save_workout/<str:name>/', views.save_workout, name='save_workout'), 
    path('add_to_workout/<str:name>/', views.add_to_workout, name='add_to_workout'),
    path('profile/', views.Profile, name='profile'),
]