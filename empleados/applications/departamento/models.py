from django.db import models


class Departamento(models.Model):
    """ Modelo para tabla departamento """

    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField(
        'Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + ' | ' + self.name + ' | ' + self.shor_name
