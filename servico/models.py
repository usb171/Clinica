from django.db import models
from core.models import Clinica

_FLAG_CHOICES = (
    ('ON', 'ON'),
    ('OFF', 'OFF'),
)

class Servico(models.Model):

    ativo = models.CharField('Serviço Ativo ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField('Nome do Serviço', max_length=120, null=True, blank=True)
    preco = models.CharField('Preço do Serviço', max_length=5, null=True, blank=True)
    tempo = models.CharField('Tempo do Serviço (em minutos)', max_length=5, null=True, blank=True)
    prazoRetorno = models.CharField('Prazo para retorno (em dias)', max_length=5, null=True, blank=True)
    prazoValidade = models.CharField('Prazo Validade (em meses)', max_length=5, null=True, blank=True)

    nomeDocumento1 = models.CharField('Nome Documento 1', max_length=250, null=True, blank=True)
    nomeDocumento2 = models.CharField('Nome Documento 2', max_length=250, null=True, blank=True)
    nomeDocumento3 = models.CharField('Nome Documento 3', max_length=250, null=True, blank=True)
    nomeDocumento4 = models.CharField('Nome Documento 4', max_length=250, null=True, blank=True)

    codeDocumento1 = models.TextField("Code Documento 1", null=True, blank=True)
    codeDocumento2 = models.TextField("Code Documento 2", null=True, blank=True)
    codeDocumento3 = models.TextField("Code Documento 3", null=True, blank=True)
    codeDocumento4 = models.TextField("Code Documento 4", null=True, blank=True)
