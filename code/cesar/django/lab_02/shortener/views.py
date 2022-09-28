import string
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

from .models import UrlShortener

# Create your views here.


def index(request: HttpRequest):
    characters = string.ascii_lowercase + string.ascii_uppercase
    if request.method == 'POST' and request.POST['url']:

        short = ''.join(random.choice(characters) for i in range(6))
        long_url = request.POST['url']
        created_url = UrlShortener(long_url=long_url, short_url=short)
        created_url.save()
    url_list = UrlShortener.objects.all()
    context = {
        'url_list': url_list
    }
    return render(request, 'index.html', context)


def reroute(request, shorts):
    redirect_url = UrlShortener.objects.get(short_url=shorts)
    return redirect(redirect_url.long_url)
