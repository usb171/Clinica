from django.urls import path
from .views import usuarios, novoUsuario


urlpatterns = [
    path('usuarios', usuarios, name='usuarios'),
    path('novoUsuario', novoUsuario, name='novoUsuario'),
]