from django.urls import path
# from .views import HomeView
from . import views


app_name = "post"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_chirp, name='add'),
    path('<str:other_user>', views.authuser_chirps, name='other_user'),
]
