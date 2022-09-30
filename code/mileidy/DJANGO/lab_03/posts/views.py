from django.shortcuts import render
from .models import *

def index(request):
    context = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            chirp_text = request.POST.get('chirp-text')
            chirp_user = request.user
            Posts.objects.create(chirp_text=chirp_text, author=chirp_user)
        else:
            context['message'] = 'You are not logged in.'
    all_chirps = Posts.objects.all()
    context['all_chirps']= all_chirps
    return render(request, 'posts/index.html', context)



def user_chirps(request, this_user):
    context = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            chirp_text = request.POST.get('chirp-text')
            chirp_user = request.user
            Posts.objects.create(chirp_text=chirp_text, author=chirp_user)
        else:
            context['message'] = 'You are not logged in.'
    this_user = User.objects.get(username=this_user)
    all_chirps = Posts.objects.filter(author=this_user)
    context['all_chirps']= all_chirps
    return render(request, 'posts/index.html', context)

