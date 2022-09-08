
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import UrlShort

def index(request):
    long_url = UrlShort.objects.all(long_url=long_url)
    context = {
        'long_url':long_url
        }
    return render(request, 'urlshort_app/index.html', context )

def submit_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('url')
        UrlShort.objects.create(long_url=long_url)
    return redirect('/')

    




    