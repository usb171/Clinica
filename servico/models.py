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

    valor1 = models.CharField('Valor 1', max_length=50, null=True, blank=True)
    porcentagem1 = models.CharField('Porcentagem 1', max_length=5, null=True, blank=True)
    quemRealiza1 = models.CharField('Quem Realiza 1 ?', max_length=120, null=True, blank=True)
    especificar1 = models.CharField('Especificar 1', max_length=120, null=True, blank=True)

    valor2 = models.CharField('Valor', max_length=50, null=True, blank=True)
    porcentagem2 = models.CharField('Porcentagem 2', max_length=5, null=True, blank=True)
    quemRealiza2 = models.CharField('Quem Realiza 2 ?', max_length=120, null=True, blank=True)
    especificar2 = models.CharField('Especificar 2', max_length=120, null=True, blank=True)

    valor3 = models.CharField('Valor 3', max_length=50, null=True, blank=True)
    porcentagem3 = models.CharField('Porcentagem 3', max_length=5, null=True, blank=True)
    quemRealiza3 = models.CharField('Quem Realiza 3 ?', max_length=120, null=True, blank=True)
    especificar3 = models.CharField('Especificar 3', max_length=120, null=True, blank=True)




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
