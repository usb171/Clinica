from django.urls import path
from .views import servico, buscarDadosServicoAjax

urlpatterns = [
    path('meusServicos', servico, name='meusServicos'),
    path('buscarDadosServicoAjax', buscarDadosServicoAjax, name='buscarDadosServicoAjax'),
]