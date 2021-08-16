import datetime
from django.db import models
from django.db.models import Q, Count, Avg, Sum


class PrestamoManager(models.Manager):
    """ Managers para el modelo prestamo """

    def libro_promedio_edades(self):
        resultado = self.filter(libro__id='1').aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edad=Sum('lector__edad'))
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'libro'
        ).annotate(
            num_prestados=Count('libro')
        )

        for r in resultado:
            print('********************************')
            print(r, r['num_prestados'])

        return resultado
