from django.shortcuts import render, redirect
import urllib.request
import json
from .models import *


# Create your views here.
from django.http import HttpResponse
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        input = request.POST['input']
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{input}'
        with urllib.request.urlopen(url)as x:
            response = json.loads(x.read().decode())
        context = {
            'definition':response[0]['meanings'][0]['definitions'][0]['definition'],
            'userinput':input
        }
        return render(request,'index.html', context )



def logout(request):
    return render(request, 'index.html')



