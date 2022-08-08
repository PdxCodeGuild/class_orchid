from django.http import HttpResponse
from django.shortcuts import render
def welcome(request):
    return render(request,'welcome.html' )

def form(request):
    return render(request,'base.html' )

def thankyou(request):
    return render(request, 'thankyou.html')