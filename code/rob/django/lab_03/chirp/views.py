from email import contentmanager
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chirp, Like, Comment, Rechirp
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    latest_chirps = Chirp.objects.order_by('-created_at')[:5]
        
    context = {'latest_chirps': latest_chirps}
    return render(request, 'chirp/index.html', context)


def new_chirp(request):
    new_chirp_text = request.POST.get('new_chirp')
    current_user = request.user
    if new_chirp_text == None:
        print('didnt work')
        print(current_user)
    print('new text: ', new_chirp_text)
    print('current user: ', type(current_user))
    new_chirp = Chirp(user=current_user, text=new_chirp_text)
    new_chirp.save()
    return redirect('/chirp')


def like_chirp(request, chirp_id):
    chirpID = Chirp.objects.get(id=chirp_id)
    user_that_liked = request.user
    userID = User.objects.get(username=user_that_liked)
    # print(chirpID.like_set.get(user=user_that_liked))
    try: 
        chirpID.like_set.get(user=user_that_liked)
        print('user in likes')
        like = Like.objects.get(user=userID)
        print(like.id)
        like.delete()
    except Like.DoesNotExist:
        print('user not in likes')
        like = Like(chirp=chirpID, user=userID)
        like.save()
    
    print(chirpID.like_set.all())
    print('chirp', chirpID)
    print('user that liked: ', user_that_liked)
    print(userID)
    
    return redirect('/chirp')


def comment_chirp(request, chirp_id):
    chirpID = Chirp.objects.get(id=chirp_id)
    user = request.user
    
    return redirect('/chirp')


def re_chirp(request, chirp_id):
    chirpID = Chirp.objects.get(id=chirp_id)
    user_that_rechirped = request.user
    userID = User.objects.get(username=user_that_rechirped)
    try: 
        chirpID.rechirp_set.get(user=user_that_rechirped)
        print('user in likes')
        re_chirp = Rechirp.objects.get(user=userID)
        print(re_chirp.id)
        re_chirp.delete()
    except Rechirp.DoesNotExist:
        print('user not in likes')
        re_chirp = Rechirp(chirp=chirpID, user=userID)
        re_chirp.save()
    return redirect('/chirp')


def user_chirps(request, chirp_user):
    user_for_id = User.objects.get(username=chirp_user)
    posts = Chirp.objects.filter(user=user_for_id)
    print(posts)
    context = {'posts': posts}

    return render(request, 'chirp/user_posts.html', context)