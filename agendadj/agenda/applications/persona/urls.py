from django.urls import path, re_path

from . import views

app_name = 'persona_app'

urlpatterns = [
    path('personas/', views.listaPersonas.as_view(), name='personas')
]
