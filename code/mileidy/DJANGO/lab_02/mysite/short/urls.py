from django.urls import path
from . import views

app_name = 'short'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:short_url>', views.redirection, name='redirection')
]