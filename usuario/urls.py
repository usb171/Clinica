from django.urls import path
from .views import *


urlpatterns = [
    path('meusUsuarios', usuario, name='meusUsuarios'),
    path('conta', conta, name='conta'),
    path('meusUsuarios', usuario, name='meusUsuarios'),
    path('buscarEmailAjax', buscarEmailAjax, name='buscarEmailAjax'),
    path('buscarDadosUsuarioAjax', buscarDadosUsuarioAjax, name='buscarDadosUsuarioAjax'),
    path('buscarDadosUsuario2Ajax', buscarDadosUsuario2Ajax, name='buscarDadosUsuario2Ajax'),
]