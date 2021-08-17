from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-categorias/', views.ListLibrosCategorias.as_view(),
         name='libros-categorias'),
    path('libros-trg/', views.ListLibrosTrg.as_view(),
         name='libros-trg'),
    path('libros-detalle/<pk>/', views.LibroDetailView.as_view(),
         name='libros-detalle'),
]
