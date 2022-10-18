from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
