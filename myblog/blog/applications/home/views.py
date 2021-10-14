import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

from applications.entrada.models import Entry

from .models import Home
from .forms import SuscribersForm, ContactForm


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos el home
        context['home'] = Home.objects.latest('created')
        context['portada'] = Entry.objects.entrada_en_portada()
        context['entradas_home'] = Entry.objects.entradas_en_home()
        context['entradas_recientes'] = Entry.objects.entradas_recientes()
        # enviar formulario de suscripciones
        context['form'] = SuscribersForm

        return context


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
