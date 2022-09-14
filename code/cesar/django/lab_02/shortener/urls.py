from django.urls import path

from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:shorts>', views.reroute, name='redirect'),
]
