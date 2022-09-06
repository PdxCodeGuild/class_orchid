from django.urls import path
from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('complete/<int:grocery_item_id>', views.complete, name= 'complete'),
    path('incomplete/<int:grocery_item_id>', views.incomplete, name= 'incomplete')
]
