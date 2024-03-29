from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Chirp

# Create your views here.

from django.http import HttpResponse

def index(request):

    all_chirps = Chirp.objects.order_by('-posted_date')

    context = {
        'all_chirps': all_chirps[:8]
    }

    if request.method == 'POST':
        post_method(request)

    return render(request, 'forum/index.html', context)

def user_view(request, user_name):
    
    user = User.objects.filter(username=user_name)[0]
    
    all_chirps = Chirp.objects.all().filter(user=user).order_by('-posted_date')

    context = {
        'all_chirps': all_chirps[:5]
    }
    
    if request.method == 'POST':
        post_method(request)
    
    return render(request, 'forum/index.html', context)

def post_method(request):
    chirp_data = request.POST.get('chirp-field')
    if chirp_data != '':
        Chirp.objects.create(content=chirp_data, user=request.user)
    else:
        print('empty field')