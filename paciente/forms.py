from django import forms
from .models import Paciente
from django.contrib.auth.models import User

class PacienteForm(forms.Form):

    ativo = forms.CharField(required=True)
    nomeCompleto = forms.CharField(required=True)
    cpf = forms.CharField(required=False)
    dataNascimento = forms.CharField(required=False)
    idade = forms.CharField(required=False)
    sexo = forms.CharField(required=False)
    estadoCivil = forms.CharField(required=False)

    profissao = forms.CharField(widget=forms.Textarea, required=False)
    observacao = forms.CharField(widget=forms.Textarea, required=False)

    telefone = forms.CharField(required=False)
    celular = forms.CharField(required=False)
    email = forms.CharField(required=False)

    cep = forms.CharField(required=False)
    numero = forms.CharField(required=False)
    rua = forms.CharField(required=False)
    quadra = forms.CharField(required=False)
    bairro = forms.CharField(required=False)
    cidade = forms.CharField(required=False)
    estado = forms.CharField(required=False)
    complemento = forms.CharField(widget=forms.Textarea, required=False)

    grupoConvenio = forms.CharField(widget=forms.Textarea, required=False)

    nomeFamiliar = forms.CharField(required=False)
    grauParentesco = forms.CharField(required=False)


    def is_valid_from_form(self):
        return super(PacienteForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        return valid