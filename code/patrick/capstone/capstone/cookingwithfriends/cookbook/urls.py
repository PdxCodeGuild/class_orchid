from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView, RecipeCreatelView, UpdateView, UserPostView, RecipeUpdateView, RecipeDeleteView

urlpatterns = [
    path('', RecipeListView.as_view(), name='cookbook-home'),
    
    path('recipe/new/', RecipeCreatelView.as_view(), name='recipe-create'),
    path('recipe/user/<str:recipe_username>/', views.C_user, name='user-posts'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('about/', views.about, name='cookbook-about'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('search_cookbook', views.search_cookbook, name='search-cookbook'),
    path('cost_filter', views.cost_filter, name='cost'),

]