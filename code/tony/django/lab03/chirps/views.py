from typing import Any, Dict
from django.shortcuts import render
from django.views import generic

from .models import Chirp

from django.contrib.auth import get_user_model

from django.views.generic.edit import FormView
from django import forms

class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['chirps'] = Chirp.objects.all().order_by('-timestamp')
        return context


class ProfileView(generic.TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['chirps'] = Chirp.objects.all().filter(authuser=get_user_model().objects.get(username=kwargs['authuser']))
        return context

class ChirpForm(forms.Form):
    body = forms.CharField()
    def chirp(self):

        # print('chirp: ', self.data.get('body'))
        pass

class ChirpView(generic.FormView):
    form_class = ChirpForm
    success_url = '/'
    model = Chirp

    def form_valid(self, form):
        form.chirp()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        c = Chirp.objects.create(authuser=request.user, chirp=form.data.get('body'))
        c.save()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)