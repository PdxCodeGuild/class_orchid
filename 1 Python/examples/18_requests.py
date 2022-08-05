''' 
URL - Uniform Resource Locator

https://mail.google.com/u/0/#inbox
protocol://subdomain.domain.tld[extension]/path/to/wherever?query_parameter='extrainfo'

'''

# python3 -m pip install requests
import requests
import json

# optional query parameters give extra information to the request
params = {
    'seed': 'erin_the_echidna',
    'results': '10',
    'nat': 'au,fr,nz',
    'inc': 'name,nat'
}

# the requests.get() method takes a url that's an API endpoint
# plus optional keyword arguments for things like query params and headers
response = requests.get('https://randomuser.me/api/', params=params, headers={'accept': 'application/json'})

# here we see that requests.get() adds our formatted query parameters to the url
print(response.url) # https://randomuser.me/api/?seed=erin_the_echidna&results=10&nat=au%2Cfr%2Cnz&inc=name%2Cnat
print(response.status_code) # 200 (success)
print(response.encoding) # utf-8 (the default encoding)


# these all do more or less the same thing, read the response body
response = json.loads(response.text)
# response = response.text)
# response = response.json()


for result in response['results']:
    print(result)
