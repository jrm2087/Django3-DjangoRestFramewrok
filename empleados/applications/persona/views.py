from django.shortcuts import render
from django.views.generic import (ListView)

from .models import Empleado


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 2
    ordering = 'first_name'
    model = Empleado


class ListByAreaEmpleado(ListView):
    """ Lista empleados de un area """
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(departamento__shor_name=area.upper())
        return lista


class ListEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name=palabra_clave.upper())
        return lista


class ListHabilidadesEmpleados(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()
