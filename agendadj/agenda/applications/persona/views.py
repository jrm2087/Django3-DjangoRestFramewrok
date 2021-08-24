from django.shortcuts import render
from django.views.generic import ListView

from .models import Person


class listaPersonas(ListView):
    template_name = 'persona/lista.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()
