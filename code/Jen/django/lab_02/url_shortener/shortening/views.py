
from django.shortcuts import render, redirect, render 
from . models import Shortening
import random
import string
from django.views import generic



def index(request):
    if request.method=="POST":
        the_url=request.POST.get("the_url")
        if the_url !=None:
            context=get_url(the_url)
            return render(request, 'shortening/index.html', context)
    return render(request, 'shortening/index.html')
    

def magic():
    letters = string.ascii_letters
    numbers = string.digits
    characters = letters + numbers
    shorty = random.choice(characters)
    count = 0
    length = 10
    while count < length:
        count += 1
        shorty = shorty + random.choice(characters)      
    return shorty
    

def get_url(the_url):
    shorty = magic()
    the_url = the_url
    shorty = shorty
    Shortening.objects.create(
        the_url=the_url, 
        shorty=shorty,
        )
    context = {
    'the_url' : the_url,
    'shorty' : shorty,
    }
    return context


def url_redirect(request,short_version):
    returned_url=Shortening.objects.all().filter(shorty=short_version)
    url = f'http://{returned_url[0]}'
    return redirect(url)

