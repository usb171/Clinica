from django.contrib import admin
from .models import HistoricoAcesso, UsuarioLogado


class UsuarioLogadoAdmin(admin.ModelAdmin):
    readonly_fields = ['user','session_key']


class HistoricoAcessoAdmin(admin.ModelAdmin):
    list_display = ['idUser', 'user', 'dataLogon']
    readonly_fields = ['idUser', 'user', 'dataLogon']
    search_fields = (
        'usuarioDado',
    )

admin.site.register(UsuarioLogado, UsuarioLogadoAdmin)
admin.site.register(HistoricoAcesso, HistoricoAcessoAdmin)