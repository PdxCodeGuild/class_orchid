from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreatelView, PostUpdateView, UserPostView
#app_name = 'chatter'
urlpatterns = [
    path('', PostListView.as_view(), name='chatter-home'),
    #path('post/<str:username>/', UserPostView.as_view(), name='user-posts'),
    path('post/<str:post_username>/', views.user, name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreatelView.as_view(), name='post-create'),
    path('about/', views.about, name='chatter-about'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

]
