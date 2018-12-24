from django.db import models
from django.contrib.auth.models import User

class HistoricoAcesso(models.Model):

    idUser = models.IntegerField(default=-1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dataLogon = models.DateTimeField('Entrou em', null=True)

    def __str__(self):
        return self.user.first_name