from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from usuario.models import Usuario
from django.shortcuts import redirect
from .models import HistoricoAcesso, Titulo
from django.utils.timezone import localtime
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError

import json


def login(request):

    if request.method == 'GET':
        return render(request, 'core/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # Faz a autenticação do usuário
        contexto = {'flag': False, 'msg': None, 'username': username, 'password': password}
        if user is not None: # Se existir acesso
            usuario = Usuario.objects.filter(user=user)[0] # Busque os dados do usuário com esse acesso
            if usuario.ativo == "ON":  # Se o usuário estiver ativo pelo administrador
                auth_login(request, user)  # Faz o login do usuário
                desired_datetime = localtime().strftime('%Y-%m-%d %H:%M:%S')
                HistoricoAcesso.objects.create(idUser=user.id, user=request.user, dataLogon=desired_datetime)

                request.session['senhaPadraoAlterada'] = usuario.senhaPadraoAlterada
                request.session['senhaPadrao'] = usuario.clinica.senhaPadrao
                request.session['logo'] = "/static/media/" + str(usuario.clinica.logo)


                if usuario.senhaPadraoAlterada:
                    return redirect('dashboard')
                else:
                    return redirect('conta')
            else:
                contexto['msg'] = "Seu acesso foi desativado pelo administrador do sistema"
                return render(request, "core/login.html", contexto)
        else:
            contexto['msg'] = "Email e Senha não correspondem"
            return render(request, "core/login.html", contexto)

def dashboard(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                user = request.user
                #print(user.get_all_permissions())
                #usuario = Usuario.objects.get(user=user)
                #request.session['logo'] = "/static/media/" + str(usuario.clinica.logo)
            except Exception as e: # Caso ocorra erros na consulta
                if request.user.is_authenticated:
                    auth_logout(request)
                    contexto = {'flag': False, 'msg': e}
                    return render(request, "core/login.html", contexto)
            return render(request, "core/dashboard.html")
        else:
            return redirect('login')

def logout(request):
    auth_logout(request)
    return redirect('login')

def handler404(request):
    return render(request, 'core/404.html', status=404)

def handler500(request):
    return render(request, 'core/404.html', status=500)



###################################################### Título ######################################################
def titulo(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            contexto = {'titulos': Titulo.objects.all()}
            return render(request, 'titulo/titulos.html', contexto)
        elif request.method == 'POST':
            # for key in request.POST.keys():
            #     print(key, " ", request.POST[key])
            clinica = Usuario.objects.get(user=request.user).clinica
            titulo = request.POST['nomeTitulo']
            status = request.POST['status']
            id_titulo = request.POST['id_titulo']
            try:
                if Titulo.objects.filter(id=id_titulo).exists():  # Caso exista o ID passado, edite esse Título
                    titulo_obj = Titulo.objects.filter(id=id_titulo)
                    titulo_obj.update(titulo=titulo, clinica=clinica, status=status)
                else:
                    Titulo.objects.create(titulo=titulo, clinica=clinica, status=status).save()
            except IntegrityError:
                return HttpResponse(json.dumps({'fail': True, 'msg': "O título " + titulo + " já existe", 'erros': {'nomeTitulo': -1 }}), content_type="application/json")
            return HttpResponse(json.dumps({'ok': True, 'msg': "Título Salvo com Sucesso!", 'erros': {}}), content_type="application/json")
    else:
        return redirect('login')

def buscarTituloAjax(request):
    if request.user.is_authenticated:
        titulo = request.GET.get('titulo', None)
        id_nomeTitulo_original = request.GET.get('id_nomeTitulo_original', None)
        if id_nomeTitulo_original == titulo:
            data = {'titulo': False}
        else:
            data = {'titulo': Titulo.objects.filter(titulo=request.GET.get('titulo', None)).exists()}
        return JsonResponse(data)
    else:
        return redirect('login')

def buscarDadosTituloAjax(request):
    if request.user.is_authenticated:
        try:
            titulo = Titulo.objects.get(id=request.GET.get('id_titulo', None))
        except:
            return redirect('login')
        data = {
            'nomeTitulo': titulo.titulo,
            'status': titulo.status,
            'id_titulo': titulo.pk,
        }
        return JsonResponse(data)
    else:
        return redirect('login')
###################################################### Título ######################################################