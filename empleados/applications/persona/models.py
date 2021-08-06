from django.db import models
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField


class Habilitades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'

    def __str__(self):
        return str(self.id) + ' | ' + self.habilidad


class Empleado(models.Model):
    """ Modelo para tabla empleado """

    JOB_CHOICES = (
        ('0', 'INGENIERO'),
        ('1', 'CONTADOR'),
        ('2', 'PSICOLOGO'),
        ('3', 'OTRO')
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilitades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name']

    def __str__(self):
        return str(self.id) + ' | ' + self.first_name + ' | ' + self.last_name
