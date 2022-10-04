from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gods/', views.gods, name='gods'),
    path('items/', views.items, name='items'),
    path('player/', views.player, name='player'),
    path('god/', views.god, name='god'),
]