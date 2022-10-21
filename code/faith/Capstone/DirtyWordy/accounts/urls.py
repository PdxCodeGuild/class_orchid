from django.urls import path
from django.shortcuts import render
from . import views
from .views import *


app_name = 'accounts'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('favs/<str:favid>/<str:wordstore>', views.favList, name='favList'),
    path('delete/<str:wordstore>/', views.delete, name='delete'),
    path('flashcards/', views.flashcards, name='flashcards'),
    
]