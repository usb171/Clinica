from django.db import models
from core.models import Clinica

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

    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True, blank=True)
    nomeCompleto = models.CharField('Nome Completo', max_length=200, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=20, null=True, blank=True)
    dataNascimento = models.CharField('Data Nascimento', max_length=20, null=True, blank=True)
    idade = models.CharField('Idade', max_length=3, null=True, blank=True)

    sexo = models.CharField('Sexo', max_length=10, choices=_SEXO_CHOICES, default="MASCULINO", null=True, blank=True)
    estadoCivil = models.CharField('Estado Civil', max_length=25, choices=_ESTADO_CIVIL_CHOICES, default="SOLTEIRO(A)", null=True, blank=True)

    profissao = models.TextField("Profissões", null=True, blank=True)
    origem = models.TextField("Origem", null=True, blank=True)
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
    grupoFamiliar = models.TextField("Familiares", null=True, blank=True)

    # fotoPerfil = models.TextField("Foto Perfil", null=True, blank=True)

    convenio1 = models.CharField('Convênio 1', max_length=240, null=True, blank=True)
    convenio2 = models.CharField('Convênio 2', max_length=240, null=True, blank=True)
    convenio3 = models.CharField('Convênio 3', max_length=240, null=True, blank=True)
    convenio4 = models.CharField('Convênio 4', max_length=240, null=True, blank=True)

    numeroCarteira1 = models.CharField('Número Carteira 1', max_length=50, null=True, blank=True)
    numeroCarteira2 = models.CharField('Número Carteira 2', max_length=50, null=True, blank=True)
    numeroCarteira3 = models.CharField('Número Carteira 3', max_length=50, null=True, blank=True)
    numeroCarteira4 = models.CharField('Número Carteira 4', max_length=50, null=True, blank=True)

    convenioValidade1 = models.CharField('Validade do Convênio 1', max_length=20, null=True, blank=True)
    convenioValidade2 = models.CharField('Validade do Convênio 2', max_length=20, null=True, blank=True)
    convenioValidade3 = models.CharField('Validade do Convênio 3', max_length=20, null=True, blank=True)
    convenioValidade4 = models.CharField('Validade do Convênio 4', max_length=20, null=True, blank=True)

    nomeFamiliar1 = models.CharField('Nome do Familiar 4', max_length=120, null=True, blank=True)
    nomeFamiliar2 = models.CharField('Nome do Familiar 4', max_length=120, null=True, blank=True)
    nomeFamiliar3 = models.CharField('Nome do Familiar 4', max_length=120, null=True, blank=True)
    nomeFamiliar4 = models.CharField('Nome do Familiar 4', max_length=120, null=True, blank=True)

    grau1 = models.CharField('Grau do Familiar 1', max_length=20, null=True, blank=True)
    grau2 = models.CharField('Grau do Familiar 2', max_length=20, null=True, blank=True)
    grau3 = models.CharField('Grau do Familiar 3', max_length=20, null=True, blank=True)
    grau4 = models.CharField('Grau do Familiar 4', max_length=20, null=True, blank=True)






