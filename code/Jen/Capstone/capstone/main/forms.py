from xml.dom.minidom import Document
from django import forms

from .models import RabbitModel

class ImageForm(forms.ModelForm):
    class Meta:
        model=RabbitModel
        fields = ['caption', 'photo',]