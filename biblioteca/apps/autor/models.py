from django.db import models

# managers
from .managers import AutorManager


class Autor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField(default=0)

    objects = AutorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombres']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
