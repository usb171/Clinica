from django.db import models
from core.models import Clinica


class Agenda(models.Model):

    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True, blank=True)

    titulo = models.CharField('Título', max_length=20, null=True, blank=True)
    dataInicio = models.CharField('Data Início', max_length=20, null=True, blank=True)
    dataFim = models.CharField('Data Fim', max_length=20, null=True, blank=True)
    paciente = models.CharField('Paciente', max_length=120, null=True, blank=True)
    servico = models.TextField("Serviços", null=True, blank=True)


