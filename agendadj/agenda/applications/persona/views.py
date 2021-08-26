from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)

from .models import Person

from .serializers import PersonSerializers


class listaPersonas(ListView):
    template_name = 'persona/lista.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializers

    def get_queryset(self):
        return Person.objects.all()


class PersonListView(TemplateView):
    template_name = 'persona/lista2.html'


class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializers

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateApiView(CreateAPIView):
    serializer_class = PersonSerializers


class PersonDetailAPIView(RetrieveAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()


class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()
