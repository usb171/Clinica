from django.urls import path
from .views import login, dashboard, logout, titulo, buscarDadosTituloAjax, buscarTituloAjax,\
    convenio, buscarConvenioAjax, buscarDadosConvenioAjax, origem, buscarOrigemAjax,\
    buscarDadosOrigemAjax, getDataHoraAjax, controleCampo
from django.contrib.auth import views as auth_views
from . import util

urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),

    path('senha/resgatar/',
         auth_views.PasswordResetView.as_view(template_name='core/email/password_reset.html'),
         name='password_reset'),

    path('senha/envio/',
         auth_views.PasswordResetDoneView.as_view(template_name='core/email/password_reset_done.html'),
         name='password_reset_done'),

    path('senha/resgatar/novaSenha/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='core/email/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('senha/resgatar/confirmacao/',
         auth_views.PasswordResetView.as_view(template_name='core/email/password_reset_complete.html'),
         name='password_reset_complete'),

    path('ativarAcesso/<uidb64>/<token>/', util.ativarAcesso, name='ativarAcesso'),


    path('configuracoes/titulos', titulo, name='titulos'),
    path('configuracoes/buscarTituloAjax', buscarTituloAjax, name='buscarTituloAjax'),
    path('configuracoes/buscarDadosTituloAjax', buscarDadosTituloAjax, name='buscarDadosTituloAjax'),

    path('configuracoes/convenios', convenio, name='convenios'),
    path('configuracoes/buscarConvenioAjax', buscarConvenioAjax, name='buscarConvenioAjax'),
    path('configuracoes/buscarDadosConvenioAjax', buscarDadosConvenioAjax, name='buscarDadosConvenioAjax'),

    path('configuracoes/origens', origem, name='origens'),
    path('configuracoes/buscarOrigemAjax', buscarOrigemAjax, name='buscarOrigemAjax'),
    path('configuracoes/buscarDadosOrigemAjax', buscarDadosOrigemAjax, name='buscarDadosOrigemAjax'),

    path('configuracoes/controleCampos', controleCampo, name='controleCampos'),

    path('core/getDataHoraAjax', getDataHoraAjax, name='getDataHoraAjax'),

]

