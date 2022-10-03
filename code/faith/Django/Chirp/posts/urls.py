from django.urls import path
from . import views

app_name = 'posts' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_post, name='add_post')
]