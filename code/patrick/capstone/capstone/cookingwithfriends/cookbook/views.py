from django.shortcuts import render, redirect
from . models import Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User

def home(request):
    context = {
        'recipe' : Recipe.objects.all()
    }
    return render(request, 'cookbook/home.html', context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'cookbook/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']

class RecipeDetailView(DetailView):
    model = Recipe
    fields = ['recipetitle', 'ingredients', 'recipelines']
    

class RecipeCreatelView(LoginRequiredMixin ,CreateView):
    model = Recipe
    fields = ['recipetitle', 'ingredients', 'recipelines' ]
    
    def form_valid(self, form):
        form.instance.ruser = self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Recipe
    fields = ['recipetitle', 'ingredients', 'recipelines']

    def form_valid(self, form):
        form.instance.ruser = self.request.user
        return super().form_valid(form)    
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.ruser:
            return True
        return False    
def about(request):
    return render(request, 'cookbook/about.html')

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/cookbook/'
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.ruser:
            return True
        return False    


class UserPostView(ListView):
    model = Recipe
    template_name = 'cookbook/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['posts'] = Post.objects.get(author= kwargs['username'])
        print(kwargs)
        return context

    def get(self, request, *args , **kwargs):
        

        ruser = super().get(request,  *args , **kwargs)
       # posts = Post.objects.get(author= kwargs['post_id'])
       # self.extra_context = {'posts': posts}
        return ruser

def C_user(request,recipe_username ):
    C_user = User.objects.get(username=recipe_username)
    context = {
        'recipes' : Recipe.objects.filter(ruser= C_user )
    }
    return render(request, 'cookbook/home.html', context)
    


def search_cookbook(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        srecipes = Recipe.objects.filter(recipetitle__contains = searched)
        singredients = Recipe.objects.filter(ingredients__contains = searched)
        
        return render(request, 'cookbook/search_cookbook.html', {'searched': searched, 'srecipes': srecipes, 'singredients': singredients})