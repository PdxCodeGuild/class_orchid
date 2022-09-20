from django.urls import path

from . import views

app_name = 'chirp'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_chirp/', views.new_chirp, name='new_chirp'),
    path('like_chirp/<int:chirp_id>/', views.like_chirp, name='like_chirp'),
    path('comment_chirp/<int:chirp_id>/', views.comment_chirp, name='comment_chirp'),
    path('re_chirp/<int:chirp_id>/', views.re_chirp, name='re_chirp'),
    path('posts/<str:chirp_user>/', views.user_chirps, name='user_chirps'),
]