from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.http import HttpResponse, HttpRequest, Http404
from .models import Chirps
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    chirps_list = Chirps.objects.all()
    # auth_list = Chirps.objects.get('auth_users')
    context = {
        'chirps_list': chirps_list,

    }
    print(chirps_list)

    return render(request, 'home.html', context)


def add_chirp(request):
    if request.method == 'POST' and request.POST['chirp']:
        chirps = request.POST.get('chirp')

    Chirps.objects.create(
        chirp=chirps,
        auth_users=request.user
    )
    return redirect('/posts/')


def authuser_chirps(request, other_user):
    context = {}
    other_user = User.objects.get(username=other_user)
    all_chirps = Chirps.objects.filter(auth_users=other_user)
    context['chirps_list'] = all_chirps
    return render(request, 'home.html', context)
