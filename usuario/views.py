from django.shortcuts import render
from usuario.models import Usuario
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.contrib.auth.models import Permission

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

import json


def conta(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                return HttpResponse(json.dumps({'ok': True, 'msg': "Atualizado com sucesso", 'erros':{}}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'ok': False, 'msg': "Erro nos seguintes campos", 'erros': form.errors}), content_type="application/json")

        else:
            form = PasswordChangeForm(request.user)
            return render(request, 'usuario/conta.html', {'form': form})

def buscarEmailAjax(request):
    if request.user.is_authenticated:
        email = request.GET.get('email', None)
        email_original = request.GET.get('email_original', None)
        if email_original == email:
            data = {'email': False}
        else:
            data = {'email': User.objects.filter(email=request.GET.get('email', None)).exists()}
        return JsonResponse(data)
    else:
        return redirect('login')

def buscarDadosUsuarioAjax(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(id=request.GET.get('id_user', None))
        except:
            return redirect('login')

        data = {
                'id_user_logado': Usuario.objects.get(user=request.user).id,
                'id_user': usuario.pk,
                'nomeCompleto': usuario.nomeCompleto,
                'email': usuario.email,
                'titulo': usuario.titulo,
                'telefone': usuario.telefone,
                'celular': usuario.celular,
                'enderecoCompleto': usuario.enderecoCompleto,
                'ativo': usuario.ativo,
                'admin': usuario.admin,
                'agendaPropria': usuario.agendaPropria,
                'controleEstoque': usuario.controleEstoque,
                'controleProntuario': usuario.controleProntuario,
                'funcionalidadeUsuario': usuario.funcionalidadeUsuario,
               }
        return JsonResponse(data)
    else:
        return redirect('login')

def usuario(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            contexto = {'usuarios': Usuario.objects.all()}
            return render(request, 'usuario/usuarios.html', contexto)
        elif request.method == 'POST':
            # for key in request.POST.keys():
            #     print(key, " ", request.POST[key])

            form = UsuarioForm(request.POST)

            if form.is_valid():
                dados = form.cleaned_data

                email = dados['email']
                celular = dados['celular']
                enderecoCompleto = dados['enderecoCompleto']
                telefone = dados['telefone']
                nomeCompleto = dados['nomeCompleto']

                titulo = dados['titulo']
                controleEstoque = dados['controleEstoque']
                controleProntuario = dados['controleProntuario']

                ativo = dados['ativo']
                admin = dados['admin']
                agendaPropria = dados['agendaPropria']

                funcionalidadeUsuario = dados['funcionalidadeUsuario']

                id_user = request.POST['id_user']

                try:
                    if Usuario.objects.filter(id=id_user).exists():# Caso exista o ID passado, edite esse Usuário
                        usuario_obj = Usuario.objects.filter(id=id_user)
                        usuario_obj.update(email=email,
                                          ativo=ativo,
                                          admin=admin,
                                          titulo=titulo,
                                          celular=celular,
                                          telefone=telefone,
                                          nomeCompleto=nomeCompleto,
                                          agendaPropria=agendaPropria,
                                          controleEstoque=controleEstoque,
                                          enderecoCompleto=enderecoCompleto,
                                          controleProntuario=controleProntuario,
                                          funcionalidadeUsuario=funcionalidadeUsuario)

                        user_obj = User.objects.filter(id=usuario_obj[0].user.id)
                        if not user_obj[0].is_staff:
                            user_obj.update(email=email, username=email, is_superuser=True if admin == "ON" else False, is_staff=False)
                        else:
                            user_obj.update(email=email, username=email, is_superuser=True if admin == "ON" else False, is_staff=True)


                    else:
                        user = User.objects.create_user(username=email, email=email, password="123")
                        user.save()
                        Usuario.objects.create(user=user,
                                               email=email,
                                               ativo=ativo,
                                               admin=admin,
                                               titulo=titulo,
                                               celular=celular,
                                               telefone=telefone,
                                               nomeCompleto=nomeCompleto,
                                               agendaPropria=agendaPropria,
                                               controleEstoque=controleEstoque,
                                               enderecoCompleto=enderecoCompleto,
                                               controleProntuario=controleProntuario,
                                               funcionalidadeUsuario=funcionalidadeUsuario).save()
                except:
                    print("Aqui")
                    return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Usuário!", 'erros': {}}), content_type="application/json")
                return HttpResponse(json.dumps({'ok': True, 'msg': "Usuário Salvo com Sucesso!", 'erros': {}}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'ok': False, 'msg':'Erro ao Tentar Concluír o Formulário', 'erros': {}}), content_type="application/json")
    else:
        return redirect('login')