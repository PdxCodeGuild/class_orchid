from django.urls import path
from . import views

app_name = 'grocery_list_app' 
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<int:grocery_items_id>/delete/', views.delete, name='delete'),
    path('<int:grocery_items_id>/completed/', views.completed, name='completed'),
]