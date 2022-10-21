from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Fav
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
import urllib.request
import json



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def profile(request):
    if request.method == 'GET':
        listfav = Fav.objects.all().filter(user=request.user)
        context = {
            'listfav':listfav,
        }
        return render(request,'profile.html', context)
    elif request.method == 'POST':
        input = request.POST['input']
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{input}'
        with urllib.request.urlopen(url)as x:
            response = json.loads(x.read().decode())
        listfav = Fav.objects.all().filter(user=request.user)
        context = {
            'listfav':listfav,
            'definition':response[0]['meanings'][0]['definitions'][0]['definition'],
            'userinput':input
        }
        return render(request,'profile.html', context )



def favList(request, favid, wordstore):
    word = Fav(favList=favid,user=request.user, wordlist = wordstore)
    word.save()
    return HttpResponseRedirect(reverse('accounts:profile'))

def delete(request, wordstore):
    delete = Fav.objects.all().filter(wordlist=wordstore, user=request.user)
    delete.delete()
    return HttpResponseRedirect(reverse('accounts:profile'))


def flashcards(request):
    listfav = Fav.objects.all().filter(user=request.user)
    context = {
            'listfav':listfav,
        }
    return render(request,'flashcards.html', context)

def logout(request):
    return render(request, 'index.html')