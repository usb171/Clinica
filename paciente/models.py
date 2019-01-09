from django.db import models

_SEXO_CHOICES = {
    ('MASCULINO', 'MASCULINO'),
    ('FEMININO', 'FEMININO')
}

_ESTADO_CIVIL_CHOICES = {
    ('SOLTEIRO(A)', 'VIUVO(A)'),
    ('CASADO(A)', 'CASADO(A)'),
    ('DIVORCIADO(A)', 'DIVORCIADO(A)'),
    ('VIUVO(A)', 'VIUVO(A)'),
}


class Paciente(models.Model):
    nomeCompleto = models.CharField('Nome Completo', max_length=120, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=20, null=True, blank=True)
    dataNascimento = models.CharField('Data Nascimento', max_length=20, null=True, blank=True)

    sexo = models.CharField('Sexo', max_length=10, choices=_SEXO_CHOICES, default="MASCULINO", null=True, blank=True)
    estadoCivil = models.CharField('Estado Civil', max_length=25, choices=_ESTADO_CIVIL_CHOICES, default="SOLTEIRO(A)", null=True, blank=True)

