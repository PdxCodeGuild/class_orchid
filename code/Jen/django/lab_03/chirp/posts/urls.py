from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('chirp_list/', views.chirp_list, name='chirp_list'),
    path('new_chirp/', views.new_chirp, name='new_chirp'),
    path('<str:username>', views.list_userchirps, name='list_userchirps'),
    path('chirp_list/', views.chirp_list, name='chirp_list'),
    path('list_userchirps/', views.list_userchirps, name='list_userchirps'),
]