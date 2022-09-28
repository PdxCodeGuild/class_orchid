from django.urls import path

from . import views

app_name = 'shorturl'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_url>', views.url_redirect, name='url_redirect'),
]