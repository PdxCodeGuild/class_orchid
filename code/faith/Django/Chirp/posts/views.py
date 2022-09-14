from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse

# Create your views here.

def index(request):
    create_post = Post.objects.order_by('datetime_created')
    context = {
        'create_post': create_post,
    }
    return render(request, 'home.html', context)

def add_post(request):
    if request.method =="POST":
        created_post = request.POST.get('post')
        Post.objects.create(new_post=created_post)
    return redirect('/posts')