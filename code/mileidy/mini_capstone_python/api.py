# url : https://opentdb.com/api.php?amount=15&difficulty=medium&type=multiple

import requests


params = {
    "current_question": 1,
    "limit": 1,
    "next_question": 2,
    "previous_question": 1,
}


response = requests.get('https://opentdb.com/api.php?amount=15&difficulty=medium&type=multiple', params = params, headers ={'accept': 'application/json'} )
questions = response.json()

#external library i used was requests