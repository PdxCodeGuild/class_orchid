from django.urls import path
from . import views

app_name = 'dirtywordy_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.logout, name='logout'),
]