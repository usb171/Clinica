from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nomeCompleto = models.CharField('Nome Completo', max_length=120, null=True, blank=True)
    titulo = models.CharField('Título', max_length=120, null=True, blank=True)
    ativo = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    agendaPropria = models.BooleanField(default=False)
    imagemPerfil = models.FileField(null=True, blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now_add=True)
