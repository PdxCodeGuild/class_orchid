# url : https://opentdb.com/api.php?amount=15&difficulty=medium&type=multiple

import requests
import json
response = requests.get('https://opentdb.com/api.php?amount=15&difficulty=medium&type=multiple')
questions = response.json()
# print(response.json())

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)