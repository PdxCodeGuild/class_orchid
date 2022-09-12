import string
import random
from turtle import goto
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from .models import Urls

# Create your views here.
def index(request):
    try:
        latest_urls = Urls.objects.latest('pub_date')
        print(latest_urls, type(latest_urls))
        context = {'latest_urls': latest_urls}
    except Urls.DoesNotExist:
        print('doesnt work')
        context = {}

    return render(request, "urlShortener/index.html", context)


def create(request):
    url = request.POST.get('url')
    short = get_short_url(url)
    url_added = Urls.objects.create(short_url=short, actual_url=url)
    print(url_added.id)
    return redirect("/")


def goTo(request, short_url):
    get_actual_url = Urls.objects.filter(short_url=short_url)
    go_to = get_actual_url[0].actual_url
    print(type(go_to))
    return redirect(go_to)


def get_short_url(long_url):
    url = long_url
    checks = ['.com', '.org', '.net', '.gov']
    fake_ext = random_ext()
    ext = ''
    for check in checks:
        if check in url:
            ext = check
    url_split = url.split(ext)

    short_url = fake_ext

    if '.' in url_split[0]:
        cut_start = url_split[0].split('.')
        short_url =  fake_ext
        return short_url

    return short_url


def random_ext():
    rand = ''
    letters = list(string.ascii_letters + string.digits)
    for l in range(9):
        rand += random.choice(letters)
    
    return rand
