from tkinter import Widget
from django import forms
from django.forms import NumberInput
from .models import *

class WorkoutInfo(forms.Form):
    # class Meta:
        # model = WorkingSet
        # fields = '__all__'
        # exclude = ['user', 'exercise']
        # widgets = {
        #     'reps': forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'reps'})),
        #     'note': forms.CharField(widget= forms.Textarea(attrs={'placeholder':'notes'})),
        #     # 'num_sets': forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'number of sets'})),
        #     # 'weight_used': forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'weight used'})),
        #     'day': forms.DateField(widget = forms.DateInput(attrs={'placeholder': 'date of workout'}))
        # }
    reps = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'reps','class':'input'}))
    num_sets = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'number of sets','class':'input'}))
    weight_used = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'weight used','class':'input'}))
    note = forms.CharField(widget= forms.Textarea(attrs={'placeholder':'notes','class':'input'}))
    day = forms.DateField(widget = forms.DateInput(attrs={'placeholder': 'date of workout','class':'input'}))

