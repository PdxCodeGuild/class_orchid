from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('complete/<int:item_id>', views.complete, name='complete'), #item_id is creator made, can be anything
    path('delete/<int:item_id>', views.delete, name='delete'),
    path('add/', views.add, name='add'),
]