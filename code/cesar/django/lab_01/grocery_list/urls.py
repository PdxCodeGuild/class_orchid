from audioop import add
from django.urls import path

from . import views

app_name = 'grocery'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('completed/<int:item_id>/', views.completed, name='completed'),
    path('undo/<int:item_id>', views.item_undo, name='undo'),
    path('delete/<int:item_id>', views.delete_item, name='delete'),
]
