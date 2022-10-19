from django.urls import path
# from .views import HomeView
from . import views


app_name = "post"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_run, name='add'),
    path('run/',views.get_runs, name='get_run'),
    path('<str:other_users>/', views.authuser_runs, name='other_users'),
]
