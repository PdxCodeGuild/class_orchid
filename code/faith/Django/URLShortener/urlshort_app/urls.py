from django.urls import path
from . import views

app_name = 'urlshort_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('submit_url', views.submit_url, name='submit_url')
]