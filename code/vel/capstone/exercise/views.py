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

def index(request, muscle):
    if request.method == 'GET':
        exercises = Exercise.objects.all().order_by('name')
        context = {
            'exercises': exercises
        }
        return render(request, 'index.html', context) 
    else:
        exercises = Exercise.objects.all().filter(muscle=request.POST.get('value'))
        context = {
            'exercises': exercises
        }
        return render(request, 'index.html', context) 