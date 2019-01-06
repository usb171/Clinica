from django.db import models

class Paciente(models.Model):
    nomeCompleto = models.CharField('Nome Completo', max_length=120, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=20, null=True, blank=True)
