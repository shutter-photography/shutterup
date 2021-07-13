from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

# Create your views here.

class Indexview(TemplateView):
    template_name = 'index.html'
