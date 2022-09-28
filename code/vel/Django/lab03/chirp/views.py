from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from . models import Chirp
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    all_chirps = Chirp.objects.order_by('-posted_date')
    context = {
        'all_chirps': all_chirps[:7]
    }

    if request.method == 'POST':
        post_method(request)

    return render(request, 'chirp/index.html', context)


def user_view(request, username):
    user = User.objects.filter(username=username)[0]
    all_chirps = Chirp.objects.all().filter(user=user).order_by('-posted_date')
    context = {
        'all_chirps': all_chirps[:7]
    }
    if request.method == 'POST':
        post_method(request)

    return render(request, 'chirp/index.html', context)


def post_method(request):
    chirp_data = request.POST.get('chirp')
    if chirp_data != '':
        Chirp.objects.create(content=chirp_data, user=request.user)
    else:
        print('No input')
