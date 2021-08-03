from django.db import models


class Departamento(models.Model):
    """ Modelo para tabla departamento """

    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField(
        'Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return str(self.id) + ' | ' + self.name + ' | ' + self.shor_name
