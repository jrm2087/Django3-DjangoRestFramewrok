from django.db import models
from django.db.models import Q


class AutorManager(models.Manager):
    """ Managers para el modelo autor """

    def listar_autores(self):
        return self.all()

    def buscar_autor(self, kword):
        resultado = self.filter(nombre__icontains=kword)
        return resultado

    def buscar_autor_or(self, kword):
        resultado = self.filter(Q(nombre__icontains=kword)
                                | Q(apellido__icontains=kword))
        return resultado

    def buscar_autor_exclude(self, kword):
        resultado = self.filter(nombre__icontains=kword).exclude(Q(edad__icontains=85)
                                                                 | Q(edad__icontains=99))
        return resultado

    def buscar_autor_and(self, kword):
        resultado = self.filter(edad__gt=80, edad__lt=100).order_by(
            'apellido', 'nombre')
        return resultado
