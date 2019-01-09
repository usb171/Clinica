from django.urls import path
from .views import paciente, buscarDadosPacienteAjax


urlpatterns = [
    path('meusPacientes', paciente, name='meusPacientes'),
    path('buscarDadosPacienteAjax', buscarDadosPacienteAjax, name='buscarDadosPacienteAjax'),

]