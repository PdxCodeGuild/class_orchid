from django.shortcuts import render
from . models import Input
from django.contrib.auth import logout


def index(request):
    if request.method=="POST":
        new_chirp(request)

    context=chirp_list()
    return render(request, "home.html", context)
 

def chirp_list():
    chirp_list = Input.objects.all()
    context = {
        "chirp_list" : chirp_list,
    }
    return context


def list_userchirps(request):
    context = get_userchirps(request)
    return render(request, "home.html", context)
  

def get_userchirps(request):
    user=request.user
    current_user=user.id
    userchirps=Input.objects.all().filter(user_id=current_user)
    context = {
        "userchirps" : userchirps,
    }
    return context


def new_chirp(request):
    new_chirp=request.POST.get("new_chirp") 
    user=request.user
    user_id=user.id
    new_chirp=Input.objects.create(
        new_chirp = new_chirp,
        user_id=user_id)
    return new_chirp
    

def log_out(request):
    logout(request)
    return render(request, 'logout')


