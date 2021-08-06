from django.urls import path

from . import views

app_name = 'persona_app'


urlpatterns = [
    path('listar-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-empleados-area/<shorname>/',
         views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades-empleado/', views.ListHabilidadesEmpleados.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(),
         name='modificar_empleado')
]
