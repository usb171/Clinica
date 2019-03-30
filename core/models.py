from django.db import models
from django.contrib.auth.models import User

_FLAG_CHOICES = (
    ('ON', 'ON'),
    ('OFF', 'OFF'),
)

_FLAG_CONTROLE_PACIENTE = (
    ('required', 'required'),
    ('no_required', 'no_required'),
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
    status = models.CharField('Título Ativo ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, null=True)
    titulo = models.CharField('Nome do Título', max_length=60, null=True, blank=True)
    created_at = models.DateTimeField('Criada em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizada em', auto_now_add=True)

    class Meta:
        unique_together = ('titulo', 'clinica',)

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
    status = models.CharField('Título Ativo ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, null=True)
    nome = models.CharField('Nome do Convênio', max_length=60, null=True, blank=True)

    class Meta:
        unique_together = ('nome', 'clinica',)

    def __str__(self):
        return self.nome

class Origem(models.Model):

    """
        A Origem é uma entidade que representa a fonte do surgimento do paciente.
    """
    status = models.CharField('Origem Ativa ?', max_length=4, choices=_FLAG_CHOICES, default="ON", null=True, blank=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, null=True)
    nome = models.CharField('Nome da Origem', max_length=60, null=True, blank=True)

    class Meta:
        unique_together = ('nome', 'clinica',)

    def __str__(self):
        return self.nome


class ControleCampo(models.Model):

    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, null=True)
    paciente_nomeCompleto = models.CharField('Paciente Nome Completo', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_cpf = models.CharField('Paciente CPF', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_sexo = models.CharField('Paciente Sexo', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_dataNascimento = models.CharField('Paciente Data de Nascimento', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_idade = models.CharField('Paciente Idade', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_estadoCivil = models.CharField('Paciente Estado Civil', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_profissao = models.CharField('Paciente Profissao', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_observacao = models.CharField('Paciente Observacao', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_telefone = models.CharField('Paciente Telefone', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_celular = models.CharField('Paciente Celular', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_email = models.CharField('Paciente email', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_cep = models.CharField('Paciente CEP', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_numero = models.CharField('Paciente Número', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_rua = models.CharField('Paciente Rua', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_quadra = models.CharField('Paciente Quadra', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_bairro = models.CharField('Paciente bairro', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_cidade = models.CharField('Paciente cidade', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_estado = models.CharField('Paciente estado', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_complemento = models.CharField('Paciente complemento', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_convenio = models.CharField('Paciente Convenio', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_convenioCarteira = models.CharField('Paciente Número Carteira', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_convenioValidade = models.CharField('Paciente Convenio Validade', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_nomeFamiliar = models.CharField('Paciente Nome Familiar', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_grauParentesco = models.CharField('Paciente Grau Parentesco', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    paciente_origem = models.CharField('Paciente Origem', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    usuario_nomeCompleto = models.CharField('Usuário Nome Completo', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    usuario_email = models.CharField('Usuário Email', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    usuario_telefone = models.CharField('Usuário Telefone', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    usuario_celular = models.CharField('Usuário Celular', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    usuario_enderecoCompleto = models.CharField('Usuário Endereço Completo', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)
    usuario_titulo = models.CharField('Usuário Título', max_length=25, choices=_FLAG_CONTROLE_PACIENTE, default="no_required", null=True, blank=True)

    def __str__(self):
        return self.clinica.nome