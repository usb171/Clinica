from django.shortcuts import render
from usuario.models import Usuario
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm
import json


def usuarios(request):
    if request.method == 'GET' and request.user.is_authenticated:
        contexto = {'usuarios': Usuario.objects.all()}
        print(contexto)
        return render(request, 'usuario/usuarios.html', contexto)
    else:
        return redirect('login')


def buscarEmailAjax(request):
    if request.user.is_authenticated:
        data = {'email': User.objects.filter(email=request.GET.get('email', None)).exists()}
        return JsonResponse(data)
    else:
        return redirect('login')

def novoUsuario(request):
    if request.method == 'POST' and request.user.is_authenticated:
        for key in request.POST.keys():
            print(key, " ", request.POST[key])

        form = UsuarioForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            email = dados['email']
            celular = dados['celular']
            telefone = dados['telefone']
            nomeCompleto = dados['nomeCompleto']

            titulo = dados['titulo']
            controleEstoque = dados['controleEstoque']
            controleProntuario = dados['controleProntuario']

            ativo = dados['ativo']
            admin = dados['admin']
            agendaPropria = dados['agendaPropria']

            try:
                user = User.objects.create_user(username=email, email=email, password="123")
                user.save()
                Usuario.objects.create(user=user, celular=celular, telefone=telefone, nomeCompleto=nomeCompleto, email=email,
                                                 titulo=titulo, controleEstoque=controleEstoque, controleProntuario=controleProntuario,
                                                 ativo=ativo, admin=admin, agendaPropria=agendaPropria).save()
            except:
                print("Ocorreu um Erro ao Criar um Novo Usuário")
                return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Usuário!", 'erros': {}}), content_type="application/json")

            return HttpResponse(json.dumps({'ok': True, 'msg': "Usuário Salvo com Sucesso!", 'erros': {}}), content_type="application/json")

        else:
            return HttpResponse(json.dumps({'ok': False, 'msg':'Erro ao Tentar Concluír o Formulário', 'erros': {}}), content_type="application/json")
