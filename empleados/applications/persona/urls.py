from django.urls import path

from . import views


urlpatterns = [
    path('listar-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-empleados-area/<shorname>/',
         views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades-empleado/', views.ListHabilidadesEmpleados.as_view())
]
