from django.urls import path
from .views import usuarios, novoUsuario, buscarEmailAjax


urlpatterns = [
    path('usuarios', usuarios, name='usuarios'),
    path('novoUsuario', novoUsuario, name='novoUsuario'),
    path('buscarEmailAjax', buscarEmailAjax, name='buscarEmailAjax'),
]