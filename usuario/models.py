from django.db import models
from django.contrib.auth.models import User

_TITULE_CHOICES = (
    ('MEDICO', 'MÉDICO'),
    ('FISIOTERAPEUTA', 'FISIOTERAPEUTA'),
    ('ENFERMEIRO', 'ENFERMEIRO'),
)

_CONTROLE_ESTOQUE_CHOICES = (
    ('VISUALIZAR', 'VISUALIZAR'),
    ('NAO_VISUALIZAR', 'NAO_VISUALIZAR'),
    ('MOVIMENTAR', 'MOVIMENTAR'),
    ('CONTROLE_TOTAL', 'CONTROLE_TOTAL'),
)

_CONTROLE_PRONTUARIO_CHOICES = (
    ('VISUALIZAR', 'VISUALIZAR'),
    ('NAO_VISUALIZAR', 'NAO_VISUALIZAR'),
    ('CONTROLE_TOTAL', 'CONTROLE_TOTAL'),
)

_ACESSO_AGENDA_CHOICES = (
    ('VISUALIZAR', 'VISUALIZAR'),
    ('NAO_VISUALIZAR', 'NAO_VISUALIZAR'),
    ('EDITAR', 'EDITAR'),
)

_ACESSO_FINANCEIRO_CHOICES = (
    ('NAO_VISUALIZAR', 'NAO_VISUALIZAR'),
    ('VISUALIZAR_DIARIO', 'VISUALIZAR_DIARIO'),
    ('VISUALIZAR_TOTAL', 'VISUALIZAR_TOTAL'),
    ('EDITAR_TOTAL', 'EDITAR_TOTAL'),
)

_ACESSO_PRONTUARIO_CHOICES = (
    ('NAO_VISUALIZAR', 'NAO_VISUALIZAR'),
    ('VISUALIZAR', 'VISUALIZAR'),
)

_FLAG_CHOICES = (
    ('ON', 'ON'),
    ('OFF', 'OFF'),
)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nomeCompleto = models.CharField('Nome Completo', max_length=120, null=True, blank=True)
    email = models.CharField('Email', max_length=120, null=True, blank=True, unique=True)
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    celular = models.CharField('Celular', max_length=20, null=True, blank=True)

    # Selects
    titulo = models.CharField('Título', max_length=25, choices=_TITULE_CHOICES, default="MÉDICO", null=True, blank=True)
    controleEstoque = models.CharField('Controle de Estoque', max_length=25, choices=_CONTROLE_ESTOQUE_CHOICES, default="NAO_VISUALIZAR", null=True, blank=True)
    controleProntuario = models.CharField('Controle de Prontuario', max_length=25, choices=_CONTROLE_PRONTUARIO_CHOICES, default="NAO_VISUALIZAR", null=True, blank=True)

    #Flags
    ativo = models.CharField('Usuário Ativo ?', max_length=25, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    admin = models.CharField('Usuário Administrador ?', max_length=25, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    agendaPropria = models.CharField('Usuário com Agenda Própria ?', max_length=25, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)


    # imagemPerfil = models.FileField(null=True, blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now_add=True)
