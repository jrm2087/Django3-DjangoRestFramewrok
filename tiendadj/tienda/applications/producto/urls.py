from django.urls import include, re_path, path

from . import views

app_name = 'producto_app'

urlpatterns = [
    path('api/producto/por-usuario/',
         views.ListProductUser.as_view(), name='producto-usuario'),
    path('api/producto/con-stok/', views.ListProductStok.as_view(),
         name='producto-con-stok'),
    path('api/producto/genero/<gender>/', views.ListProducGenero.as_view(),
         name='producto-genero'),
]
