from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import requests
from pprint import pprint
import urllib3
from django.http import HttpResponse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def token_response(request):
    auth_url = "https://www.strava.com/oauth/token"

    payload = {
        'client_id': '95093',
        'client_secret': 'cd5c86fe0a0a72e91064e06b6cc83c048a90bf3f',
        'refresh_token': 'b31d26a77c81b482620171e7aec26cd08c121b83',
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

    for i, runs in enumerate(response):
        # print(i, runs)
        name_of_run = response[i]['name']
        distance_of_run = response[i]['distance']
        distance_of_run_in_miles = distance_of_run/1609.344
        date_of_run = response[i]['start_date']
        polyline_map_of_run = response[i]['map']['summary_polyline']
        print(name_of_run, distance_of_run_in_miles, date_of_run, polyline_map_of_run)

    return HttpResponse(response)

    