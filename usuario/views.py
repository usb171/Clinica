from django.shortcuts import render
from usuario.models import Usuario
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm
from core.models import Titulo
from core.util import enviarAtivador
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

import json


def conta(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                usuario = Usuario.objects.get(user=user)
                usuario.senhaPadraoAlterada = True
                usuario.save()
                update_session_auth_hash(request, user)  # Important!
                return HttpResponse(json.dumps({'ok': True, 'msg': "Atualizado com sucesso", 'erros': {}}), content_type="application/json")
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
            'id_user': usuario.pk,
            'email': usuario.email,
            'ativo': usuario.ativo,
            'admin': usuario.admin,
            'titulo': usuario.titulo.titulo if usuario.titulo is not None else "",
            'celular': usuario.celular,
            'telefone': usuario.telefone,
            'nomeCompleto': usuario.nomeCompleto,
            'agendaPropria': usuario.agendaPropria,
            'controleEstoque': usuario.controleEstoque,
            'enderecoCompleto': usuario.enderecoCompleto,
            'controleProntuario': usuario.controleProntuario,
            'funcionalidadeUsuario': usuario.funcionalidadeUsuario,
            'id_user_logado': Usuario.objects.get(user=request.user).id,
        }
        return JsonResponse(data)
    else:
        return redirect('login')


def usuario(request):
    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica

        if request.method == 'GET':
            contexto = {
                'usuarios': Usuario.objects.filter(clinica=clinica),
                'titulos': Titulo.objects.filter(clinica=clinica),
            }
            # print(contexto)
            return render(request, 'usuario/usuarios.html', contexto)
        elif request.method == 'POST':
            # for key in request.POST.keys():
            #     print(key, " ", request.POST[key])

            form = UsuarioForm(request.POST)

            if form.is_valid():
                dados = form.cleaned_data
                email = dados['email']
                ativo = dados['ativo']
                admin = dados['admin']
                titulo = Titulo.objects.get(clinica=clinica, titulo=dados['titulo'])
                celular = dados['celular']
                telefone = dados['telefone']
                id_user = request.POST['id_user']
                nomeCompleto = dados['nomeCompleto']
                agendaPropria = dados['agendaPropria']
                controleEstoque = dados['controleEstoque']
                enderecoCompleto = dados['enderecoCompleto']
                controleProntuario = dados['controleProntuario']
                funcionalidadeUsuario = dados['funcionalidadeUsuario']

                user = None
                usuario_obj = None

                try:
                    if Usuario.objects.filter(id=id_user).exists():  # Caso exista o ID passado, edite esse Usuário
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
                        usuario = Usuario.objects.get(user=request.user)
                        clinica = usuario.clinica
                        user = User.objects.create_user(username=email, email=email, password=clinica.senhaPadrao, is_active=False)
                        clinica = Usuario.objects.filter(user=request.user)[0].clinica  # Busca a clínica em que o novo usuário será alocado
                        usuario_obj = Usuario.objects.create(user=user,
                                                             email=email,
                                                             ativo=ativo,
                                                             admin=admin,
                                                             titulo=titulo,
                                                             celular=celular,
                                                             clinica=clinica,
                                                             telefone=telefone,
                                                             nomeCompleto=nomeCompleto,
                                                             agendaPropria=agendaPropria,
                                                             controleEstoque=controleEstoque,
                                                             enderecoCompleto=enderecoCompleto,
                                                             controleProntuario=controleProntuario,
                                                             funcionalidadeUsuario=funcionalidadeUsuario)
                        user.save()
                        usuario_obj.save()

                        enviarAtivador(user=user, request=request, form=form) # Envia um email com um link de ativação da comnta

                except KeyError as e:
                    user.delete()
                    usuario_obj.delete()
                    return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Usuário! " + e, 'erros': {e}}),
                                        content_type="application/json")
                return HttpResponse(json.dumps({'ok': True, 'msg': "Usuário Salvo com Sucesso!", 'erros': {}}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'ok': False, 'msg': 'Erro ao Tentar Concluír o Formulário', 'erros': {}}), content_type="application/json")
    else:
        return redirect('login')
