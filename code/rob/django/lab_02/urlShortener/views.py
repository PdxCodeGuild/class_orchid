import string
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Urls

# Create your views here.
def index(request):
    try:
        latest_urls = Urls.objects.latest('pub_date')
        if latest_urls is not None:
            print(latest_urls, type(latest_urls))
            context = {'latest_urls': latest_urls}
        else:
            print('latest urls was empty')
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


def get_short_url(long_url):
    url = long_url
    checks = ['.com', '.org', '.net', '.gov']
    fake_ext = random_ext()
    ext = ''
    for check in checks:
        if check in url:
            ext = check
    url_split = url.split(ext)

    short_url = url_split[0] + ext + '/' + fake_ext

    if '.' in url_split[0]:
        cut_start = url_split[0].split('.')
        short_url = cut_start[1] + ext + '/' + fake_ext
        return short_url

    return short_url


def random_ext():
    rand = ''
    letters = list(string.ascii_letters + string.digits)
    for l in range(9):
        rand += random.choice(letters)
    
    return rand