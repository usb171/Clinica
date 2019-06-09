from django.urls import path
from .views import *

urlpatterns = [
    path('meusServicos', servico, name='meusServicos'),
    path('buscarDadosServicoAjax', buscarDadosServicoAjax, name='buscarDadosServicoAjax'),
    path('buscarDadosServico2Ajax', buscarDadosServico2Ajax, name='buscarDadosServico2Ajax'),
    path('buscarInformacaoGeralServicoAjax', buscarInformacaoGeralServicoAjax, name='buscarInformacaoGeralServicoAjax'),
]