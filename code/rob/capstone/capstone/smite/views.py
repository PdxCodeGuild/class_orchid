from smite.models import Skin, Session
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import requests
import hashlib
import json
with open('hide.json') as f:
    data = json.load(f)
dev_id = data['DEV_ID']
auth_key = data['AUTH_KEY']

# Create your views here.
date_utc = datetime.utcnow()
date = date_utc.strftime('%Y%m%d%H%M%S')

def index(request):
    session_id = Session.objects.get(getter_id=1)
    print('sess id', session_id)
    sig = f'{dev_id}testsession{auth_key}{date}'
    sig_hashed = hashlib.md5(sig.encode()).hexdigest()
    test_response = requests.get(f'https://api.smitegame.com/smiteapi.svc/testsessionjson/{dev_id}/{sig_hashed}/{session_id}/{date}').json()
    
    if(test_response.startswith('Invalid session id')):
        print('created session')
        sig = f'{dev_id}createsession{auth_key}{date}'
        sig_hashed = hashlib.md5(sig.encode()).hexdigest()
        response = requests.get(f'https://api.smitegame.com/smiteapi.svc/createsessionjson/{dev_id}/{sig_hashed}/{date}').json()
        Session.objects.all().delete()
        sess = Session(getter_id=1,session_id=response['session_id'])
        sess.save()
        print(sess)
        
    else:
        response = test_response
    
    
    print(test_response, response)
    context = {'dev': dev_id, 'auth': auth_key, 
        'hashed': sig_hashed, 'time': date, 'res': response, 'sess': session_id}
    return render(request, 'smite/index.html', context)


def gods(request):
    session_id = Session.objects.get(getter_id=1)
    sig = f'{dev_id}getgods{auth_key}{date}'
    sig_hashed = hashlib.md5(sig.encode()).hexdigest()
    response = requests.get(f'https://api.smitegame.com/smiteapi.svc/getgodsjson/{dev_id}/{sig_hashed}/{session_id}/{date}/1').json()
    context = {'res': response, 'sess': session_id}
    return render(request, 'smite/gods.html', context)


def items(request):
    session_id = Session.objects.get(getter_id=1)
    sig = f'{dev_id}getitems{auth_key}{date}'
    sig_hashed = hashlib.md5(sig.encode()).hexdigest()
    response = requests.get(f'https://api.smitegame.com/smiteapi.svc/getitemsjson/{dev_id}/{sig_hashed}/{session_id}/{date}/1').json()
    context = {'res': response, 'sess': session_id}
    return render(request, 'smite/items.html', context)


def player(request):
    return HttpResponse('player')


def god(request, r_id):
    session_id = Session.objects.get(getter_id=1)
    sig = f'{dev_id}getgods{auth_key}{date}'
    sig_hashed = hashlib.md5(sig.encode()).hexdigest()
    response = requests.get(f'https://api.smitegame.com/smiteapi.svc/getgodsjson/{dev_id}/{sig_hashed}/{session_id}/{date}/1').json()
    god = {}
    for res in response:
        if res['id'] == r_id:
            god = res
    context = {'res': response, 'sess': session_id, 'god': god}
    return render(request, 'smite/god.html', context)