from django.shortcuts import render
from .models import *
from string import ascii_letters, digits
from random import choices
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('url')
        all_char = list(ascii_letters + digits)
        short_url = ''.join(choices(all_char, k=6))
        Short.objects.create(long_url = long_url, short_code = short_url)
    floofy = Short.objects.all()
    context = {'all_urls' : floofy }
    return render(request, 'short/index.html', context)

def redirection(request, short_url):
    this_url = Short.objects.get(short_code = short_url)
    redir_url = this_url.long_url
    return HttpResponseRedirect(redir_url)
