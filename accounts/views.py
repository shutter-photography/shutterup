from django.contrib.auth import login,logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms


class Customersignup(CreateView):
    form_class = forms.Customercreateform
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'
