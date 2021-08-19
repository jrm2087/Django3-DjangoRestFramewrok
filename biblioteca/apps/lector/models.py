from django.db import models

from apps.libro.models import Libro
from apps.autor.models import Persona

from .managers import PrestamoManager


class Lector(Persona):
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def save(self, *args, **kwargs):
        self.libro.stok = self.libro.stok - 1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        ordering = ['libro']

    def __str__(self):
        return self.libro.titulo
