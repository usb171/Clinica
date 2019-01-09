from django.contrib import admin
from .models import HistoricoAcesso, Convenio

class HistoricoAcessoAdmin(admin.ModelAdmin):
    list_display = ['idUser', 'user', 'dataLogon']
    readonly_fields = ['idUser', 'user', 'dataLogon']
    search_fields = (
        'usuarioDado',
    )

class ConvenioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numeroCarteira']
    search_fields = (
        'nome',
        'numeroCarteira',
    )

admin.site.register(HistoricoAcesso, HistoricoAcessoAdmin)
admin.site.register(Convenio, ConvenioAdmin)