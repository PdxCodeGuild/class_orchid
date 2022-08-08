from django.urls import path
from . import views

app_name = 'OrderUp_app' 
urlpatterns = [
    path('form/', views.form, name='form'),
    path('thankyou/',views.thankyou, name='thankyou'),
    path('', views.welcome, name='welcome')
]