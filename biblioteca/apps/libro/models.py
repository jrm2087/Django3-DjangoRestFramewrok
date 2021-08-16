from django.db import models

from apps.autor.models import Autor

# managers
from .managers import LibroManager, CategoriaManager


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    objects = CategoriaManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
        return f'{str(self.id)} - {self.nombre}'


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de Lanzamiento')
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField()

    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return f'{str(self.id)} - {self.titulo}'
