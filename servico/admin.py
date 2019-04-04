from django.contrib import admin

from .models import Servico

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = (
        'nome',
    )


admin.site.register(Servico, ServicoAdmin)
