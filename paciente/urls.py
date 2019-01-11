from django.urls import path
from .views import paciente, buscarDadosPacienteAjax, buscarEmailAjax


urlpatterns = [
    path('meusPacientes', paciente, name='meusPacientes'),
    path('buscarDadosPacienteAjax', buscarDadosPacienteAjax, name='buscarDadosPacienteAjax'),
    path('buscarEmailAjax', buscarEmailAjax, name='buscarEmailAjax'),
]