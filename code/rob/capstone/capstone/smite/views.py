from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'smite/index.html')


def gods(request):
    return HttpResponse('gods')


def items(request):
    return HttpResponse('items')


def player(request):
    return HttpResponse('player')


def god(request):
    return HttpResponse('god')