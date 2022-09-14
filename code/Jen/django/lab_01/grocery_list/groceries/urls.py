from django.urls import path
from . import views

app_name = 'groceries'

urlpatterns = [
    path('', views.index),
    path('delete/<int:id>', views.delete),
    path('shopped/<int:id>', views.shopped),

]