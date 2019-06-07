from django.urls import path
from .views import *

urlpatterns = [
    path('meusServicos', servico, name='meusServicos'),
    path('buscarDadosServicoAjax', buscarDadosServicoAjax, name='buscarDadosServicoAjax'),
    path('buscarInformacaoGeralServicoAjax', buscarInformacaoGeralServicoAjax, name='buscarInformacaoGeralServicoAjax'),
]