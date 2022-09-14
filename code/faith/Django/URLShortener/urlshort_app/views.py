
from random import choice
from string import ascii_letters
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import UrlShort

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_url = ''.join([choice(ascii_letters) for x in range(8)])
        UrlShort.objects.create(short_url=short_url, long_url=long_url)
    context = {
        'all_urls': UrlShort.objects.all()
    }
    return render(request, 'urlshort_app/index.html', context)


def url_redirect(request, short_url):
    redirect_url = get_object_or_404(UrlShort, short_url=short_url)
    long_url = redirect_url.long_url
    return HttpResponseRedirect(long_url)




    