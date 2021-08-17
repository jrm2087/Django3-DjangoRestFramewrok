from django.shortcuts import render
from django.views.generic import ListView, DetailView

# models
from .models import Libro


class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        f1 = self.request.GET.get('fecha1', '')
        f2 = self.request.GET.get('fecha2', '')

        if f1 and f2:
            return Libro.objects.listar_libros_fecha(palabra_clave, f1, f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)


class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        return Libro.objects.listar_libros_trg(palabra_clave)


class ListLibrosCategorias(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista_categoria.html'

    def get_queryset(self):
        parametro = 3
        return Libro.objects.listar_libros_categorias(parametro)


class LibroDetailView(DetailView):
    template_name = 'libro/detalle.html'
    model = Libro
