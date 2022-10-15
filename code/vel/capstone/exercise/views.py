from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse

from .models import Exercise, Muscle

# class ExerciseListView(ListView):
#     model = Exercise
#     template_name = 'index.html'

#     def get_queryset(self):
#         return Exercise.objects.order_by('name')

def index(request):
    # if request.method == 'GET':
    #     exercises = Exercise.objects.all().order_by('name')
    #     context = {
    #         'exercises': exercises
    #     }
    if request.method == 'POST':
        muscle = Muscle.objects.get(name=request.POST['user_exercise_search'])
        context = {
            'exercises': muscle.exercise.all()
        }
        return render(request, 'index.html', context) 
    return render(request, 'index.html') 