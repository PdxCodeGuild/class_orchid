
from django.shortcuts import render, redirect
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'chatter/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'chatter/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content']
    

class PostCreatelView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

def about(request):
    return render(request, 'chatter/about.html')


class UserPostView(ListView):
    model = Post
    template_name = 'chatter/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['posts'] = Post.objects.get(author= kwargs['username'])
        print(kwargs)
        return context

    def get(self, request, *args , **kwargs):
        

        user = super().get(request,  *args , **kwargs)
       # posts = Post.objects.get(author= kwargs['post_id'])
       # self.extra_context = {'posts': posts}
        return  user

def user(request,post_username ):
    user = User.objects.get(username=post_username)
    context = {
        'posts' : Post.objects.filter(author= user )
    }
    return render(request, 'chatter/home.html', context)
    


          
        
