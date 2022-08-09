import random
from api import questions
import json
from pprint import pprint

print('Hello and welcome to Quizzer!')

user_name = input('Please enter your name below \n: ').title()

starter = input(f'Hello {user_name}! Would you like to begin the game? (y/n) \n: ')
pprint(questions['results'][0]['question'].replace('&quot;', '"').replace('&#039;', "'"))

# def random_question_gen():
#     question_generator = []




# random_question_gen()


# while True:
#     if starter == 'yes':

