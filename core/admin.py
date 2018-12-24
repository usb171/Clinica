from django.contrib import admin
from .models import HistoricoAcesso

class HistoricoAcessoAdmin(admin.ModelAdmin):
    list_display = ['idUser', 'user', 'dataLogon']
    readonly_fields = ['idUser', 'user', 'dataLogon']
    search_fields = (
        'usuarioDado',
    )

admin.site.register(HistoricoAcesso, HistoricoAcessoAdmin)