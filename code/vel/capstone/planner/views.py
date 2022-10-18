from django.shortcuts import render
from .models import Workout, WorkingSet
from exercise.models import Muscle, Exercise
from users.models import CustomUser
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    now = datetime.now()
    monday = now - timedelta(now.weekday())
    sunday = now + timedelta((6-now.weekday())%7)
    workout_objects = Workout.objects.filter(day__range = [monday,sunday])
    context = {
        'workout_objects': workout_objects
    }
    return render(request, 'index.html', context) 
    ...

def workout(request, date):
    try: 
        this_workout = Workout.objects.get(day = date) 
        # get working set objects related to this_workout
    except ObjectDoesNotExist:
        Workout.objects.create(day = date , user = request.user)

    ...
        # add objects to context dict like line 14
        # add the ability to add notes to each day 

def add_to_workout(request):
    ...
        # use drop down selector, add the ability to add rep, sets, weight.




