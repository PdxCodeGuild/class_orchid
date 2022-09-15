from django.urls import path

from . import views

# app_name = ''

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('chirp', views.ChirpView.as_view(), name='chirp'),
    path('<str:authuser>', views.ProfileView.as_view(), name='profile'),
]