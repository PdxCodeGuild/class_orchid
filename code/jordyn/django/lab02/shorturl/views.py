from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from random import randint, seed

from .models import ShortURL

# Create your views here.

def index(request):

    if request.method == 'POST':
        new_url = request.POST['add_url']
        seed(new_url)
        
        try: #Thanks Matt
            ShortURL.objects.get(long_url=new_url)
        except: #if does not exist, error is raised.
            if new_url != '': #ignores empty fields
                ShortURL.objects.create( #fills in model data
                    long_url=new_url,
                    short_url=url_return(),
                )

        #Written by me
        # if new_url != '': #ignores empty fields
        #     ShortURL.objects.create( #fills in model data
        #         long_url=new_url,
        #         short_url=url_return(),
        #     )

    short_urls = ShortURL.objects.all()
    context = {
        'urls':short_urls,
    }    
    return render(request, 'index.html', context)

def url_return(): #returns string
    string_count = 12
    keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
    short_string = url_string(string_count, keys)

    url_all = ShortURL.objects.all()
    url_lists = []

    for url in url_all:
        url_lists.append(url.short_url)

    while short_string in url_lists:
        short_string = url_string(string_count, keys)

    return short_string

def url_string(string_count, keys): #Creates a short unique string
    loop = 0
    url = ''
    while loop < string_count:
        rand_int = randint(0, len(keys) - 1)
        url += keys[rand_int]
        loop += 1
    return url

def url_redirect(request, short_url):
    this_redirect = get_object_or_404(ShortURL, short_url=short_url)
    return redirect(this_redirect.long_url)
