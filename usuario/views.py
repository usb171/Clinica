from django.shortcuts import render
from usuario.models import Usuario
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm
import json


# def usuarios(request):
#     if request.user.is_authenticated:
#         contexto = {'usuarios': Usuario.objects.all()}
#         return render(request, 'usuario/usuarios.html', contexto)
#     else:
#         return redirect('login')



def buscarEmailAjax(request):
    if request.user.is_authenticated:
        email = request.GET.get('email', None)
        email_original = request.GET.get('email_original', None)
        if email_original == email:
            data = {'email': False}
        else:
            data = {'email': User.objects.filter(email=request.GET.get('email', None)).exists()}

        #print(email, " ", email_original, " flag: ", data['email'])
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
                        User.objects.filter(id=usuario_obj[0].user.id).update(email=email, username=email)

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