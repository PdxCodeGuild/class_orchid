from django.urls import path
from . import views

app_name = 'grocery_list_app' 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:grocery_items_id>/', views.grocery_list, name='grocery_list'),
    path('<int:grocery_items_id>/completed/', views.completed, name='completed'),
]