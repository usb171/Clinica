from django.contrib import admin
from .models import HistoricoAcesso, Convenio, Clinica, Titulo, Origem, ControleCampo

class HistoricoAcessoAdmin(admin.ModelAdmin):
    list_display = ['idUser', 'user', 'dataLogon']
    readonly_fields = ['idUser', 'user', 'dataLogon']
    search_fields = (
        'usuarioDado',
    )

class ConvenioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'clinica']
    search_fields = (
        'nome',
        'clinica__nome'
    )

class ClinicaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuarioAdmin']
    search_fields = (
        'nome',
        'usuarioAdmin',
    )

class OrigemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'clinica']
    search_fields = (
        'nome',
        'clinica__nome',
    )

class TituloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'clinica']
    search_fields = (
        'titulo',
        'clinica__nome',
    )

class ControleCampoAdmin(admin.ModelAdmin):
    list_display = ['clinica']
    search_fields = (
        'clinica__nome',
    )

admin.site.register(HistoricoAcesso, HistoricoAcessoAdmin)
admin.site.register(Convenio, ConvenioAdmin)
admin.site.register(Clinica, ClinicaAdmin)
admin.site.register(Titulo, TituloAdmin)
admin.site.register(Origem, OrigemAdmin)
admin.site.register(ControleCampo, ControleCampoAdmin)