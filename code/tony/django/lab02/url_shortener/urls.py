from django.urls import path

from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:sc>', views.RedirectView.as_view(), name='redirect'),
]