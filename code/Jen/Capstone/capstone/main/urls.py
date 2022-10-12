from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

path('', views.home, name='home'),
path('hotots/', views.hotots, name='hotots'),
path('rex/', views.rex, name='rex'),
path('gallery/', views.gallery, name='gallery'),


]





