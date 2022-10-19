from django import forms
from django.forms import ModelForm
from .models import *

class WorkoutInfo(forms.ModelForm):
    class Meta:
        model = WorkingSet
        fields = '__all__'
        exclude = ['user']


