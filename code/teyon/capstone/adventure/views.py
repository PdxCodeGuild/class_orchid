from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import Profile
from django.contrib.auth.models import User

def index(request):
    # all_comments = Comment.objects.order_by('-posted_date')
    # context = {
    #     'all_comments': all_comments[:10]
    # }

    # if request.method == 'POST':
    #     post_method(request)

    return render(request, 'capstone.html')


def profile(request):
    print(request.user)
    flightInfo = Profile.objects.all().filter(user=request.user)
    print(flightInfo)
    context = {
        'flightInfo': flightInfo
    }
    return render(request, 'profile.html', context)

def flights(request,arv,des,pri):
    savedFlightData = Profile(user=request.user, price=pri, departing=des, arriving=arv)
    savedFlightData.save()
    return HttpResponseRedirect(reverse('adventure:profile'))

# def user_view(request, username):
#     user = User.objects.filter(username=username)[0]
#     all_comments = Comment.objects.all().filter(user=user).order_by('-posted_date')
#     context = {
#         'all_comments': all_comments[10]
#     }

#     if request.method == 'POST':
#         post_method(request)


# def post_method(request):
    # comment_data = request.POST.get('comment')
    # if comment_data != '':
    #     Comment.objects.create(content=comment_data, user=request.user)
    # else:
    #     print("no input")