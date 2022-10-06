from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserForm
from django.views.generic import DetailView
from django.contrib.auth.forms import *
from .models import CustomUser
from django.shortcuts import get_object_or_404


class SignUpView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class IndexView(CreateView):
    form_class = UserForm
    # success_url = reverse_lazy('')
    template_name = 'index.html'

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user_profile'
    def get_object(self):
        return get_object_or_404(CustomUser, username = self.kwargs['username'])