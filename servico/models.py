from django.db import models
from core.models import Clinica
from usuario.models import Usuario

_FLAG_CHOICES = (
    ('ON', 'ON'),
    ('OFF', 'OFF'),
)

class Servico(models.Model):

    ativo = models.CharField('Serviço Ativo ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True, blank=True)


    nome = models.CharField('Nome do Serviço', max_length=120, null=True, blank=True)
    preco = models.CharField('Preço do Serviço', max_length=50, null=True, blank=True)
    tempo = models.CharField('Tempo do Serviço (em minutos)', max_length=5, null=True, blank=True)



    rateio1 = models.CharField('Rateio 1', max_length=50, null=True, blank=True)
    titulo1 = models.CharField('Quem Recebe ? 1', max_length=120, null=True, blank=True)
    tipoRateio1 = models.CharField('Tipo Rateio 1', max_length=5, null=True, blank=True)

    rateio2 = models.CharField('Rateio 2', max_length=50, null=True, blank=True)
    titulo2 = models.CharField('Quem Recebe ? 2', max_length=120, null=True, blank=True)
    tipoRateio2 = models.CharField('Tipo Rateio 2', max_length=5, null=True, blank=True)

    rateio3 = models.CharField('Rateio 3', max_length=50, null=True, blank=True)
    titulo3 = models.CharField('Quem Recebe ? 3', max_length=120, null=True, blank=True)
    tipoRateio3 = models.CharField('Tipo Rateio 3', max_length=5, null=True, blank=True)

    rateio4 = models.CharField('Rateio 4', max_length=50, null=True, blank=True)
    titulo4 = models.CharField('Quem Recebe ? 4 ', max_length=120, null=True, blank=True)
    tipoRateio4 = models.CharField('Tipo Rateio 4', max_length=5, null=True, blank=True)

    rateio5 = models.CharField('Rateio 5', max_length=50, null=True, blank=True)
    titulo5 = models.CharField('Quem Recebe ? 5', max_length=120, null=True, blank=True)
    tipoRateio5 = models.CharField('Tipo Rateio 5', max_length=5, null=True, blank=True)

    rateio6 = models.CharField('Rateio 6', max_length=50, null=True, blank=True)
    titulo6 = models.CharField('Quem Recebe ? 6', max_length=120, null=True, blank=True)
    tipoRateio6 = models.CharField('Tipo Rateio 6', max_length=5, null=True, blank=True)


    prazoRetorno = models.CharField('Prazo para retorno (em dias)', max_length=5, null=True, blank=True)
    prazoValidade = models.CharField('Prazo Validade (em meses)', max_length=5, null=True, blank=True)


    nomeDocumento1 = models.CharField('Nome Documento 1', max_length=250, null=True, blank=True)
    nomeDocumento2 = models.CharField('Nome Documento 2', max_length=250, null=True, blank=True)
    nomeDocumento3 = models.CharField('Nome Documento 3', max_length=250, null=True, blank=True)
    nomeDocumento4 = models.CharField('Nome Documento 4', max_length=250, null=True, blank=True)
    nomeDocumento5 = models.CharField('Nome Documento 4', max_length=250, null=True, blank=True)
    nomeDocumento6 = models.CharField('Nome Documento 4', max_length=250, null=True, blank=True)

    codeDocumento1 = models.TextField("Code Documento 1", null=True, blank=True)
    codeDocumento2 = models.TextField("Code Documento 2", null=True, blank=True)
    codeDocumento3 = models.TextField("Code Documento 3", null=True, blank=True)
    codeDocumento4 = models.TextField("Code Documento 4", null=True, blank=True)
    codeDocumento5 = models.TextField("Code Documento 5", null=True, blank=True)
    codeDocumento6 = models.TextField("Code Documento 6", null=True, blank=True)
