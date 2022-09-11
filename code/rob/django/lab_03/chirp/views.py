from unittest import mock
from django.shortcuts import render
from django.http import HttpResponse
from .models import Chirp, Like, Comment, Rechirp

# Create your views here.
def index(request):
    latest_chirps = Chirp.objects.order_by('-created_at')[::5]
    
        
    context = {'latest_chirps': latest_chirps}
    return render(request, 'chirp/index.html', context)