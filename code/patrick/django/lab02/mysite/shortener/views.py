

from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect

from .forms import UrlForm
from django.template import loader
from .models import Shortener


def index(request):
    urllist = Shortener.objects.order_by("id")

    form = UrlForm()

    context = {"urllist":urllist, "form":form}
    template = loader.get_template("shortener/index.html")
    return HttpResponse(template.render(context, request))

def addurl(request):
    form = UrlForm(request.POST)

    if form. is_valid():
        new_url = Shortener(longurl = request.POST.get("text"))
        
        
        new_url.save()

        return (redirect(reverse("shortener:index")))
    

def reredirect(request, shortcode):
    sc = Shortener.objects.get(shortcode = shortcode)
    return (redirect(sc.longurl))