from django.contrib import admin
from .models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nomeCompleto']
    #readonly_fields = ['user', 'nomeCompleto']
    search_fields = (
        'nomeCompleto',
    )


admin.site.register(Paciente,PacienteAdmin)
