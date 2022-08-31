from django.shortcuts import render

from class_orchid.code.vel.Django.lab01 import grocery_list


# Create your views here.

def index(request):

    return render(request, 'grocery_list/index.html')

