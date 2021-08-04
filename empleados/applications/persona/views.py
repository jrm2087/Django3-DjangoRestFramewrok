from django.shortcuts import render
from django.views.generic import (ListView)

from .models import Empleado


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado


class ListByAreaEmpleado(ListView):
    """ Lista empleados de un area """
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(departamento__shor_name=area.upper())
        return lista
