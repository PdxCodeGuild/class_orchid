from django.shortcuts import render, redirect
from .models import RabbitModel
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, "home.html",)

def hotots(request):
    return render(request, "hotots.html",)

def rex(request):
    return render(request, "rex.html",)


def upload(request):
   form=ImageForm(request.POST or None, request.FILES or None)
   if form.is_valid():
        form.save()
   

def gallery(request):
    if request.method=="POST":
        upload(request)
    photos = RabbitModel.objects.all
    context = {
    "photos" : photos,
        }

    return render(request, 'gallery.html', context)




