from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:this_user>', views.user_chirps, name='user_chirps'),
]
