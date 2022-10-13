from django import forms
from django.contrib.auth.models import User
from .models import Recipe



class RecipeUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ['picture']