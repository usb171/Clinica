from django.urls import path
from .views import *


urlpatterns = [
    path('meusPacientes', paciente, name='meusPacientes'),
    path('buscarDadosPacienteAjax', buscarDadosPacienteAjax, name='buscarDadosPacienteAjax'),
    path('buscarDadosPaciente2Ajax', buscarDadosPaciente2Ajax, name='buscarDadosPaciente2Ajax'),
    path('buscarEmailAjax', buscarEmailAjax, name='buscarEmailAjax'),
]