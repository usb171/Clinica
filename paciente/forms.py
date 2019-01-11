from django import forms
from .models import Paciente
from django.contrib.auth.models import User

class PacienteForm(forms.Form):

    nomeCompleto = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    dataNascimento = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    estadoCivil = forms.CharField(required=True)

    profissao = forms.CharField(widget=forms.Textarea, required=True)
    observacao = forms.CharField(widget=forms.Textarea, required=False)

    telefone = forms.CharField(required=False)
    celular = forms.CharField(required=True)
    email = forms.CharField(required=True)

    cep = forms.CharField(required=False)
    numero = forms.CharField(required=False)
    rua = forms.CharField(required=True)
    quadra = forms.CharField(required=False)
    bairro = forms.CharField(required=True)
    cidade = forms.CharField(required=True)
    estado = forms.CharField(required=True)
    complemento = forms.CharField(widget=forms.Textarea, required=True)

    grupoConvenio = forms.CharField(widget=forms.Textarea)


    def is_valid_from_form(self):
        return super(PacienteForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        return valid