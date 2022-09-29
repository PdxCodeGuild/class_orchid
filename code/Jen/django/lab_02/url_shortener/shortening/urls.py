from django.urls import path

from . import views

app_name = 'shortening'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_url', views.get_url, name='get_url'),

    path('<str:short_version>', views.url_redirect, name='url_redirect'),

]

