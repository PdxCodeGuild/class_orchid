from os import access
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.http import HttpResponse, HttpRequest, Http404
from .models import Log
from django.contrib.auth.models import User
import requests


def index(request):
    run_list = Log.objects.all()
    # auth_list = Log.objects.get('auth_users')

    context = {
        'run_list': run_list,
    }
    print(run_list)
    return render(request, 'home.html', context)


def add_run(request):
    if request.method == 'POST' and request.POST['add']:
        log = request.POST.get('add')

        Log.objects.create(
            log_post=log,
            auth_users=request.user)

    return redirect('/posts/')


def authuser_runs(request, other_users):
    context = {}
    user = User.objects.get(username=other_users)
    all_runs = Log.objects.filter(auth_users=user)
    context['run_list'] = all_runs
    return render(request, 'home.html', context)


def get_access_token(request):

    user_access_token = request.GET.get('code')
    # print(request.GET.get('code'))

    url_for_refresh_token = 'https://www.strava.com/oauth/token'

    payload = {
        'client_id': '95093',
        'client_secret': 'cd5c86fe0a0a72e91064e06b6cc83c048a90bf3f',
        'code': user_access_token,
        'grant_type': 'authorization_code',
    }

    post_refresh_token = requests.post(
        url_for_refresh_token, data=payload, verify=False)

    user_refresh_token = post_refresh_token.json().get('refresh_token')

    print(user_refresh_token)

    Log.objects.update_or_create(auth_users=user_refresh_token)

    return HttpResponse(user_access_token)


def get_runs(request):
    auth_url = "https://www.strava.com/oauth/token"

    payload = {
        'client_id': '95093',
        'client_secret': 'cd5c86fe0a0a72e91064e06b6cc83c048a90bf3f',
        'refresh_token': '52643195ddf9524b853914d4ff8ac00335ab222c',
        'grant_type': 'refresh_token',
    }

    print("requesting token \n")

    res = requests.post(auth_url, data=payload, verify=False)

    access_token = res.json()['access_token']

    print("Access Token: {}".format(access_token))

    activities_url = "https://www.strava.com/api/v3/athlete/activities"

    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}

    response = requests.get(
        activities_url, headers=header, params=param).json()

    print(type(response))

    for i, runs in enumerate(response):
        # print(i, runs)
        name_of_run = response[i]['name']
        distance_of_run = response[i]['distance']
        distance_of_run_in_miles = distance_of_run/1609.344
        date_of_run = response[i]['start_date']
        # polyline_map_of_run = response[i]['map']['summary_polyline']
        print(name_of_run, distance_of_run_in_miles,
              date_of_run)

    context = {
        'run_list': response

    }
    print(context)

    return render(request, 'runs.html', context)


def delete_post(request):
    if request.method == 'POST' and request.POST['delete']:
        delete_post = request.POST.get('delete')

    Log.objects.delete

    return redirect('/posts/')




 