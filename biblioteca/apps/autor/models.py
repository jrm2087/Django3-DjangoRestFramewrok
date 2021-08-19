from django.db import models

# managers
from .managers import AutorManager


class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    class Meta:
        abstract = True


class Autor(Persona):
    seudonimo = models.CharField(
        'seudonimo', max_length=50, blank=True, null=True)

    objects = AutorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
