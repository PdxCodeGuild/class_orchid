from django.urls import path
from . import views

app_name = "shortener"
urlpatterns = [
    path("", views.index, name= "index"),
    path("addurl/", views.addurl, name= "addurl"),
    path("<slug:shortcode>", views.reredirect, name= "reredirect"),
]