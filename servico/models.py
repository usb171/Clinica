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
    preco = models.CharField('Preço do Serviço', max_length=50, null=True, blank=True)
    tempo = models.CharField('Tempo do Serviço (em minutos)', max_length=5, null=True, blank=True)
    quantSessao = models.CharField('Quantidade de Sessões', max_length=50, null=True, blank=True)


    rateio_1 = models.CharField('Rateio 1', max_length=50, null=True, blank=True)
    titulo_1 = models.CharField('Quem Recebe ? 1', max_length=120, null=True, blank=True)
    tipoRateio_1 = models.CharField('Tipo Rateio 1', max_length=5, null=True, blank=True)

    rateio_2 = models.CharField('Rateio 2', max_length=50, null=True, blank=True)
    titulo_2 = models.CharField('Quem Recebe ? 2', max_length=120, null=True, blank=True)
    tipoRateio_2 = models.CharField('Tipo Rateio 2', max_length=5, null=True, blank=True)

    rateio_3 = models.CharField('Rateio 3', max_length=50, null=True, blank=True)
    titulo_3 = models.CharField('Quem Recebe ? 3', max_length=120, null=True, blank=True)
    tipoRateio_3 = models.CharField('Tipo Rateio 3', max_length=5, null=True, blank=True)

    rateio_4 = models.CharField('Rateio 4', max_length=50, null=True, blank=True)
    titulo_4 = models.CharField('Quem Recebe ? 4 ', max_length=120, null=True, blank=True)
    tipoRateio_4 = models.CharField('Tipo Rateio 4', max_length=5, null=True, blank=True)

    rateio_5 = models.CharField('Rateio 5', max_length=50, null=True, blank=True)
    titulo_5 = models.CharField('Quem Recebe ? 5', max_length=120, null=True, blank=True)
    tipoRateio_5 = models.CharField('Tipo Rateio 5', max_length=5, null=True, blank=True)

    rateio_6 = models.CharField('Rateio 6', max_length=50, null=True, blank=True)
    titulo_6 = models.CharField('Quem Recebe ? 6', max_length=120, null=True, blank=True)
    tipoRateio_6 = models.CharField('Tipo Rateio 6', max_length=5, null=True, blank=True)


    prazoRetorno = models.CharField('Prazo para retorno (em dias)', max_length=5, null=True, blank=True)
    prazoValidade = models.CharField('Prazo Validade (em meses)', max_length=5, null=True, blank=True)


    nomeDocumento_1 = models.CharField('Nome Documento 1', max_length=250, null=True, blank=True)
    nomeDocumento_2 = models.CharField('Nome Documento 2', max_length=250, null=True, blank=True)
    nomeDocumento_3 = models.CharField('Nome Documento 3', max_length=250, null=True, blank=True)
    nomeDocumento_4 = models.CharField('Nome Documento 4', max_length=250, null=True, blank=True)
    nomeDocumento_5 = models.CharField('Nome Documento 4', max_length=250, null=True, blank=True)
    nomeDocumento_6 = models.CharField('Nome Documento 4', max_length=250, null=True, blank=True)

    codeDocumento_1 = models.TextField("Code Documento 1", null=True, blank=True)
    codeDocumento_2 = models.TextField("Code Documento 2", null=True, blank=True)
    codeDocumento_3 = models.TextField("Code Documento 3", null=True, blank=True)
    codeDocumento_4 = models.TextField("Code Documento 4", null=True, blank=True)
    codeDocumento_5 = models.TextField("Code Documento 5", null=True, blank=True)
    codeDocumento_6 = models.TextField("Code Documento 6", null=True, blank=True)
