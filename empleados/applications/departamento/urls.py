from django.urls import path
from . import views


urlpatterns = [
    path('new-departamento/', views.newDepartamentoView.as_view(),
         name='nuevo_departamento')
]
