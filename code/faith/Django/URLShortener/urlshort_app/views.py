
from gc import get_objects
from multiprocessing import context
from random import choice
from string import ascii_letters
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import UrlShort

def index(request):
    if request.method =="POST":
        long_url = request.POST('long_url')
        # short_url = submit_url()
        UrlShort.objects.create(long_url=long_url)
        return render(request, 'urlshort_app/index.html')


# def submit_url(request):
#     if request.method == 'POST':
#         long_url = request.POST.get('url')
#         UrlShort.objects.create(long_url=long_url)
#     return redirect('/')

def submit_url():
    return ''.join([choice(ascii_letters)for x in range (8)])

def redirect():
    new_url = get_object_or_404(UrlShort)
    return HttpResponseRedirect(new_url.long_url)





    