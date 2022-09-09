
from logging import PlaceHolder
from django import forms


class UrlForm(forms.Form):
    text = forms.CharField(max_length=200,
        widget = forms.TextInput(attrs={"id" : "myinput", "placeholder" : "add a new url to shorten"}))