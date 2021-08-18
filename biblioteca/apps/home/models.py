from django.db import models


class Persona(models.Model):
    """ Modelo persona """

    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('pais', max_length=30)
    pasaporte = models.CharField('pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('apelativo', max_length=10)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ['pais', 'apelativo']
        constraints = [models.CheckConstraint(
            check=models.Q(edad__gte=18), name='edad_mayor_18')]
        abstract = True

    def __str__(self):
        return self.full_name


class Empleado(Persona):
    empleo = models.CharField('Empleo', max_length=50)


class Cliente(Persona):
    email = models.EmailField('Email')
