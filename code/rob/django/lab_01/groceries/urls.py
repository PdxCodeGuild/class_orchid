from unicodedata import name
from django.urls import path
from . import views

app_name = 'groceries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('completed/<int:item_id>/', views.completed, name='completed'),
    path('undo/<int:item_id>/', views.undo, name='undo'),
]