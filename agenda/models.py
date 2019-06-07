from django.db import models
from core.models import Clinica
from usuario.models import Usuario
from paciente.models import Paciente


class Agenda(models.Model):

    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True, blank=True)

    titulo = models.CharField('Título', max_length=20, null=True, blank=True)
    dataInicio = models.CharField('Data Início', max_length=20, null=True, blank=True)
    horaInicio = models.CharField('Hora Início', max_length=20, null=True, blank=True)
    dataFim = models.CharField('Data Fim', max_length=20, null=True, blank=True)
    horaFim = models.CharField('Hora Fim', max_length=20, null=True, blank=True)
    data = models.CharField('Data', max_length=20, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    profissional = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    servico = models.TextField("Serviços", null=True, blank=True)


