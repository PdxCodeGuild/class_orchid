from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post

def index(request):
    create_post = Post.objects.order_by('datetime_created')
    context = {
        'create_post':create_post,
    }
    return render(request, 'posts.html', context)

def add_post(request):
    if request.method == "POST":
        created_post = request.POST.get('post')
        Post.objects.create(new_post=created_post, user=request.user)
        # user = request.POST.get()
    return redirect('/posts/')


def delete(request, poststore):
    print(poststore)
    delete = Post.objects.all().filter(new_post=poststore, user=request.user)
    print(delete)
    delete.delete()
    return HttpResponseRedirect(reverse('posts:index'))