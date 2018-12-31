from django.urls import path
from .views import usuario, buscarEmailAjax, buscarDadosUsuarioAjax


urlpatterns = [
    path('meusUsuarios', usuario, name='meusUsuarios'),
    path('buscarEmailAjax', buscarEmailAjax, name='buscarEmailAjax'),
    path('buscarDadosUsuarioAjax', buscarDadosUsuarioAjax, name='buscarDadosUsuarioAjax'),
]