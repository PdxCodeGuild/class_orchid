from django.shortcuts import render, redirect, reverse
from .models import WorkingSet
from exercise.models import Muscle, Exercise
from users.models import CustomUser
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.http import HttpResponseRedirect


# def index(request):
#     now = datetime.now()
#     monday = now - timedelta(now.weekday())
#     sunday = now + timedelta((6-now.weekday())%7)
#     workout_objects = WorkingSet.objects.filter(day__range = [monday,sunday])
#     context = {
#         'workout_objects': workout_objects
#     }
#     return render(request, 'index.html', context) 
#     ...


def add_to_workout(request, name):
    exercise = Exercise.objects.get(name = name)
    form = WorkoutInfo()
    context = {
        'workout': exercise.name,
        'description': exercise.description,
        'form': form
    }
    return render(request, 'users/add-form.html', context)
    ...
        # use drop down selector, add the ability to add rep, sets, weight.


def save_workout(request, name):
    if request.method == 'POST':
        form = WorkoutInfo(request.POST) 
        exercise = Exercise.objects.get(name = name)
        print(exercise)
        print(form)
        planner_object = WorkingSet.objects.create(
            exercise = exercise,
            reps = form.cleaned_data['reps'],
            num_sets = form.cleaned_data['num_sets'],
            weight_used = form.cleaned_data['weight_used'],
            day = form.cleaned_data['day'],
            user = request.user,
            note = form.cleaned_data['note'],
        )
        #  create planner object in database, ()
        return HttpResponseRedirect(reverse('planner:profile'))
    
def Profile(request):
    users_workout = WorkingSet.objects.all().filter(user=request.user)
    context = {
        'users_workout': users_workout,
    }
    return render(request, 'users/profile.html', context)
