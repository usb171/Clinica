from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nomeCompleto']
    #readonly_fields = ['user', 'nomeCompleto']
    search_fields = (
        'nomeCompleto',
    )


admin.site.register(Usuario,UsuarioAdmin)
