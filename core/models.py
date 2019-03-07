from django.db import models
from django.contrib.auth.models import User

_FLAG_CHOICES = (
    ('ON', 'ON'),
    ('OFF', 'OFF'),
)

class Clinica(models.Model):
    """
        A Clínica é uma entidade que tem como escopo um estabelecimento médico que será referência
        para outras entidades como Convênio, Paciente, Usuário. Com ela, é possível mapear outras
        entidades, Por exemplo: Paciente de ID 20 pertence à Clínica de ID 9 pois na entidade paci-
        ente existe uma chave extrangeira identificando qual clína tal paciente pertence.

        Importante: Somente o administrador MASTER (Usuário com acesso ao servidor do banco de dados)
        tem o acesso para criar, modificar e desativar uma clínica.
    """
    ativo = models.CharField('Clínica Ativa ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    usuarioAdmin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nome = models.CharField('Nome da Clínica', max_length=60, null=True, blank=True)
    senhaPadrao = models.CharField('Senha Padrão', max_length=60, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=60, null=True, blank=True)
    logo = models.FileField(null=True, blank=True)

    created_at = models.DateTimeField('Criada em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizada em', auto_now_add=True)

    def __str__(self):
        return self.nome


class Titulo(models.Model):
    """
        A Classe Título é uma entidade que tem como escopo a definição de um cargo de um funcionário de uma clínica
    """
    status = models.CharField('Clínica Ativa ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField('Nome do Título', max_length=60, null=True, blank=True)
    created_at = models.DateTimeField('Criada em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizada em', auto_now_add=True)

    def __str__(self):
        return self.titulo

class HistoricoAcesso(models.Model):

    idUser = models.IntegerField(default=-1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dataLogon = models.DateTimeField('Entrou em', null=True)

    def __str__(self):
        return self.user.first_name

class Convenio(models.Model):

    """
        O Convênio é uma entidade que representa um plano de saúde.
    """

    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True)
    nome = models.CharField('Nome do Convênio', max_length=60, null=True, blank=True)
    numeroCarteira = models.CharField('Número da Carteira', max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nome

