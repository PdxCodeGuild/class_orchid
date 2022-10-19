from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
from django.http import HttpResponse
from .models import Token
from django.contrib.auth.models import User
from django.shortcuts import redirect, render 


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def token_response(request):

    auth_url = "https://www.strava.com/oauth/token"
 
    payload = {
        'client_id': '95093',
        'client_secret': 'cd5c86fe0a0a72e91064e06b6cc83c048a90bf3f',
        'refresh_token': '52643195ddf9524b853914d4ff8ac00335ab222c',
        'grant_type': 'refresh_token',
    }

    print("requesting token \n")

    res = requests.post(auth_url, data=payload, verify=False)
    # pprint(res.json())

    access_token = res.json()['access_token']

    print("Access Token: {}".format(access_token))

    activities_url = "https://www.strava.com/api/v3/athlete/activities" 

    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}

    response = requests.get(
        activities_url, headers=header, params=param).json()

    print(type(response))

    # for i, runs in enumerate(response):
    #     # print(i, runs)
    #     name_of_run = New_Post.objects.create(name=response[i]['name'])
    #     distance_of_run = New_Post.objects.create(distance=response[i]['distance'])
    #     date_of_run = New_Post.objects.create(time=response[i]['start_date'])
    #     type_of_run = New_Post.objects.create(name=response[i]['type'])# polyline_map_of_run = response[i]['map']['summary_polyline']
        
    #     post_info = New_Post.objects.all()
    #     print(post_info)
    return HttpResponse(response)


def get_access_token(request):

    user_auth_code = request.GET.get('code')
    # print(request.GET.get('code'))

    url_for_refresh_token = 'https://www.strava.com/oauth/token'

    payload = {
        'client_id': '95093',
        'client_secret': 'cd5c86fe0a0a72e91064e06b6cc83c048a90bf3f',
        'code': user_auth_code,
        'grant_type': 'authorization_code',
    }
    print(user_auth_code)
    post_refresh_token = requests.post(
        url_for_refresh_token, data=payload, verify=False)

    user_refresh_token = post_refresh_token.json().get('refresh_token')

    print(user_refresh_token)
    Token.objects.update_or_create(refresh_token=user_refresh_token, user=request.user)

    return redirect('/posts/run')
