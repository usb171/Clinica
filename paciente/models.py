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

    nomeCompleto = models.CharField('Nome Completo', max_length=120, null=True, blank=True)
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
    # atualizacaoFotoPerfil = models.CharField('Atualização Foto Perfil', max_length=240, null=True, blank=True)


    # fotoConvenio1A = models.TextField("Foto Convênio 1A", null=True, blank=True)
    # atualizacaoConvenio1A = models.CharField('Atualização Foto Convênio 1A', max_length=240, null=True, blank=True)
    # fotoConvenio1B = models.TextField("Foto Convênio 1B", null=True, blank=True)
    # atualizacaoConvenio1B = models.CharField('Atualização Foto Convênio 1B', max_length=240, null=True, blank=True)
    #
    # fotoConvenio2A = models.TextField("Foto Convênio 2A", null=True, blank=True)
    # atualizacaoConvenio2A = models.CharField('Atualização Foto Convênio 2A', max_length=240, null=True, blank=True)
    # fotoConvenio2B = models.TextField("Foto Convênio 2B", null=True, blank=True)
    # atualizacaoConvenio2B = models.CharField('Atualização Foto Convênio 2B', max_length=240, null=True, blank=True)
    #
    # fotoConvenio3A = models.TextField("Foto Convênio 3A", null=True, blank=True)
    # atualizacaoConvenio3A = models.CharField('Atualização Foto Convênio 3A', max_length=240, null=True, blank=True)
    # fotoConvenio3B = models.TextField("Foto Convênio 3B", null=True, blank=True)
    # atualizacaoConvenio3B = models.CharField('Atualização Foto Convênio 3B', max_length=240, null=True, blank=True)
    #
    # fotoConvenio4A = models.TextField("Foto Convênio 4A", null=True, blank=True)
    # atualizacaoConvenio4A = models.CharField('Atualização Foto Convênio 4A', max_length=240, null=True, blank=True)
    # fotoConvenio4B = models.TextField("Foto Convênio 4B", null=True, blank=True)
    # atualizacaoConvenio4B = models.CharField('Atualização Foto Convênio 4B', max_length=240, null=True, blank=True)




    # nomeFamiliar = models.CharField('Nome do Familiar', max_length=120, null=True, blank=True)
    # grauParentesco = models.CharField('Grau de Parentesco', max_length=120, null=True, blank=True)






