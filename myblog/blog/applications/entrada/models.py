from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import EntryManager


class Category(TimeStampedModel):
    short_name = models.CharField('Nombre corto', max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen', upload_to='Entry', blank=True, null=True)
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title
