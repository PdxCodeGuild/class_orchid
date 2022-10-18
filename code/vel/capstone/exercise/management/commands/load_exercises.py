import json
from django.core.management.base import BaseCommand
from ...models import Exercise, Muscle
import re

class Command(BaseCommand):
    def handle(self, *args, **options):
        Exercise.objects.all().delete()
        Muscle.objects.all().delete()
        category = {
            10: "Abs",
            8: "Arms",
            12: "Back",
            14: "Calves",
            11: "Chest",
            9: "Legs",
            13: "Shoulders",
        }
        with open('exercises.json')as f:
            exercise_list = json.loads(f.read())

            for exercise in exercise_list['exercises']:
                exer_obj = Exercise.objects.create(
                    name = exercise['name'],
                    description = exercise["description"].replace('<p>','').replace('</p>','').replace('<em>','').replace('</em>','').replace('<io>','').replace('</io>','').replace('<li>','').replace('</li>','').replace('<ul>','').replace('</ul>','').replace('<ol>','').replace('</ol>','')
                )
                print(category[exercise['category']])
                
                muscle_obj,created = Muscle.objects.get_or_create(name=category[exercise['category']]) 
                muscle_obj.exercise.add(exer_obj)

# im trying to translate the muscle keyword to the number assigned to the muscle group from the api
# if i input the word it is in my exercise database with the name and description but i cant translate from string to int
                