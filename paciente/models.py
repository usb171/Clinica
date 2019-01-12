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

_FLAG_CHOICES = (
    ('ON', 'ON'),
    ('OFF', 'OFF'),
)

class Paciente(models.Model):

    ativo = models.CharField('Paciente Ativo ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)


    nomeCompleto = models.CharField('Nome Completo', max_length=120, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=20, null=True, blank=True)
    dataNascimento = models.CharField('Data Nascimento', max_length=20, null=True, blank=True)

    sexo = models.CharField('Sexo', max_length=10, choices=_SEXO_CHOICES, default="MASCULINO", null=True, blank=True)
    estadoCivil = models.CharField('Estado Civil', max_length=25, choices=_ESTADO_CIVIL_CHOICES, default="SOLTEIRO(A)", null=True, blank=True)

    profissao = models.TextField("Profissões", null=True, blank=True)
    observacao = models.TextField("Observação", null=True, blank=True)

    email = models.CharField('Email', max_length=120, null=True, blank=True, unique=True)
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    celular = models.CharField('Celular', max_length=20, null=True, blank=True)

    cep = models.CharField('CEP', max_length=20, null=True, blank=True)
    numero = models.CharField('Número', max_length=240, null=True, blank=True)
    rua = models.CharField('Rua', max_length=240, null=True, blank=True)
    quadra = models.CharField('Quadra', max_length=240, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=240, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=240, null=True, blank=True)
    estado = models.CharField('Estado', max_length=240, null=True, blank=True)
    complemento = models.TextField("Complemento", null=True, blank=True)

    grupoConvenio = models.TextField("Convenios", null=True, blank=True)

    nomeFamiliar = models.CharField('Nome do Familiar', max_length=120, null=True, blank=True)
    grauParentesco = models.CharField('Grau de Parentesco', max_length=120, null=True, blank=True)






