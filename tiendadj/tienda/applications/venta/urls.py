from django.urls import re_path, path

from . import views

app_name = 'venta_app'

urlpatterns = [
    path('api/venta/reporte', views.ReportVentasLista.as_view(), name='venta-reporte'),
    path('api/venta/create', views.RegistrarVenta.as_view(), name='venta-registro'),
    path('api/venta/add', views.RegistrarVenta2.as_view(), name='venta-add')
]
