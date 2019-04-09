from django import forms
from .models import Usuario
from django.contrib.auth.models import User

class UsuarioForm(forms.Form):

    #user = forms.OneToOneField(required=True)
    nomeCompleto = forms.CharField(required=True)
    email = forms.CharField(required=True)
    telefone = forms.CharField(required=False)
    celular = forms.CharField(required=True)
    enderecoCompleto = forms.CharField(required=True)

    # Selects
    titulo = forms.CharField(required=True)
    controleEstoque = forms.CharField(required=True)
    controleProntuario = forms.CharField(required=True)

    # Flags
    ativo = forms.CharField(required=True)
    admin = forms.CharField(required=True)
    agendaPropria = forms.CharField(required=True)

    funcionalidadeUsuario = forms.CharField(widget=forms.Textarea)

    def is_valid_from_form(self):
        return super(UsuarioForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not valid:
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            return False
        # elif User.objects.filter(email=self.cleaned_data['email']).exists():
        #     self.add_error(field='email', error='Email já cadastrado')
        #     return False
        return valid