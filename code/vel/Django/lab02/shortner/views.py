from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import ShortLink
import random, string
# Create your views here.

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        ShortLink.objects.create(
            long_url=long_url,
            short_code=short_code,
        )
    all_links = ShortLink.objects.all()
    context = {
        'all_links': all_links,
    }
    return render(request, 'index.html', context)

def forwarder(request, short_code):
    this_link = get_object_or_404(ShortLink, short_code=short_code)
    return redirect(this_link.long_url)