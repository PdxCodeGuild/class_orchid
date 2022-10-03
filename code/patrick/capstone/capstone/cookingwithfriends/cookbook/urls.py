from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView, RecipeCreatelView, UpdateView, UserPostView, RecipeUpdateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='cookbook-home'),
    
    path('recipe/new/', RecipeCreatelView.as_view(), name='recipe-create'),
    path('recipe/user/<str:recipe_username>/', views.C_user, name='user-posts'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('about/', views.about, name='cookbook-about'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),

]