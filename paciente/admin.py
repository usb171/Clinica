from django.contrib import admin
from .models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nomeCompleto', 'clinica']
    #readonly_fields = ['user', 'nomeCompleto']
    search_fields = (
        'nomeCompleto',
    )


admin.site.register(Paciente,PacienteAdmin)
