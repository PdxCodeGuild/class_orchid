from django.urls import path
from . import views

app_name = 'posts' 
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_post, name='add_post'),
    path('delete/<str:poststore>', views.delete, name='delete')
]