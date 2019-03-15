from django.db import models
from django.contrib.auth.models import User

class HistoricoAcesso(models.Model):

    idUser = models.IntegerField(default=-1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dataLogon = models.DateTimeField('Entrou em', null=True)

    def __str__(self):
        return self.user.first_name

class Convenio(models.Model):

    nome = models.CharField('Nome do Convênio', max_length=60, null=True, blank=True)
    numeroCarteira = models.CharField('Número da Carteira', max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nome