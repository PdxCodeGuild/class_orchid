from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('complete/<int:id>', views.complete, name ='complete'),
    path('undo/<int:id>', views.undo, name ='undo'),
    path('add/', views.add, name = 'add'),
]
