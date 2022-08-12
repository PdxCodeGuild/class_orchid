import requests, json, pprint 

api_key = '1073ce4606cd8c09f89ca186d81ab75f'
response = requests.get('https://favqs.com/api/typeahead', headers={'accept':'application/json'})

# response = json.loads(response.text)

print(response)