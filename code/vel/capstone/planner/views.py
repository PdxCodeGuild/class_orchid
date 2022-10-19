from django.shortcuts import render
from .models import Workout, WorkingSet
from exercise.models import Muscle, Exercise
from users.models import CustomUser
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from .forms import *


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
        # get WorkingSet objects related to this_workout
    except ObjectDoesNotExist:
        Workout.objects.create(day = date , user = request.user)

    ...
    context = {
        'this_workout': this_workout
    }
    return render(request, 'index.html', context)
        # add objects to context dict like line 14
        # add the ability to add notes to each day 

def add_to_workout(request, name, desc):
    form = WorkoutInfo()
    context = {
        'form': form
    }

    print(name,desc)

    return render(request, 'users/add-form.html', context)
    ...
        # use drop down selector, add the ability to add rep, sets, weight.


def save_workout(request):
    ...

