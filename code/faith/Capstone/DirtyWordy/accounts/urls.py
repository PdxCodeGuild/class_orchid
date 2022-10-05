from django.urls import path
from django.shortcuts import render
from .views import SignUpView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    
]