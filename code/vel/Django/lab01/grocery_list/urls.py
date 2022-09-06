from django.urls import path

from . import views


#item_id will be used as my second argument in my views function
urlpatterns = [
    path('', views.index, name = "index"),
    path('add_item/', views.add_item),
    path('<int:item_id>/remove_item/', views.remove_item),
    path('<int:item_id>/complete/', views.complete),
    path('<int:item_id>/incomplete/', views.incomplete),
]