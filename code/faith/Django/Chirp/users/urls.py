from django.urls import path
from . import views

app_name = 'users' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]