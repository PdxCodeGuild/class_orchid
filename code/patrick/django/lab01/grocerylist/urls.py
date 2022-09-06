from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("add", views.additem, name = "add"),
    path("complete/<item_id>", views.completeitem, name = "complete"),
    path("deleteitem/<item_id>", views.deleteitem, name = "deleteitem"),
    path("deleteall", views.deleteall, name = "deleteall"),
    path("undoitem/<item_id>", views.undoitem, name = "undoitem"),
]
