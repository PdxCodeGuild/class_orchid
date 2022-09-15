
from django.shortcuts import render, HttpResponse,redirect
from .models import urlModel
import random
from django.http import Http404
def home(request):
    return render(request, "homepage.html")

def makeshorturl(request):
    if request.method=='POST':
        longurl = request.POST['longurl']
        abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ"
        shorturl = ("".join(random.sample(abc,10)))
        obj = urlModel.objects.create(longurl=longurl,shorturl=shorturl)
        print("object created")
        shorturl = "http://localhost:8000/urlshortener/"+shorturl

    return HttpResponse("Your short url for {} is {} ".format(longurl,shorturl))


def redirecturl (request,shorturl):
    print(shorturl)
    obj = urlModel.objects.get(shorturl=shorturl)
    print(obj==True)

    if obj != None:
        print("object found")
        print(obj.longurl)
        return redirect(obj.longurl)

    else:
        return Http404
