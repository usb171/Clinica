from django.contrib import admin

from .models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    search_fields = (
        'titulo',
    )


admin.site.register(Agenda, AgendaAdmin)
