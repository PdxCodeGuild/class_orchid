from django.urls import path

from . import views

app_name = 'shortening'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_url', views.get_url, name='get_url'),
    path('get_it_back', views.get_it_back, name ='get_it_back'),
   
    
]

