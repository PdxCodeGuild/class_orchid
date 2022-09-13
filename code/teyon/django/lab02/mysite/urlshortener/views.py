from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import urlModel
import random
def home(request):
    return render(request, "homepage.html")

def makeshorturl(request):
    if request.method=='POST':
        longurl = request.POST['longurl']
        abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ!@#$"
        shorturl = ("".join(random.sample(abc,10)))
        obj = urlModel.objects.create(longurl=longurl,shorturl=shorturl)
        print("object created")

    return HTTPResponse("request recieved")