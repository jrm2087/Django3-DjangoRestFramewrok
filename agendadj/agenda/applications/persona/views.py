from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)

from .models import Person, Reunion

from .serializers import (
    PersonSerializers,
    PersonaSerializers,
    PersonaSerializers2,
    ReunionSerializers,
    PersonaSerializers3,
    ReunionSerializersLink,
    PersonPagination,
    CountReunionSerializer)


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


class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()


class PersonRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()


class PersonApiLista(ListAPIView):
    # serializer_class = PersonaSerializers
    serializer_class = PersonaSerializers3

    def get_queryset(self):
        return Person.objects.all()


class ReunionApiLista(ListAPIView):
    serializer_class = ReunionSerializers

    def get_queryset(self):
        return Reunion.objects.all()


class ReunionApiListaLink(ListAPIView):
    serializer_class = ReunionSerializersLink

    def get_queryset(self):
        return Reunion.objects.all()


class PersonApiListaPaginacion(ListAPIView):
    """ Lista personas con paginacion"""
    serializer_class = PersonaSerializers
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class ReunionByPersonJobs(ListAPIView):
    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
