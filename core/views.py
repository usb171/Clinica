from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from usuario.models import Usuario
from django.shortcuts import redirect
from .models import HistoricoAcesso
from django.utils.timezone import localtime




def login(request):

    if request.method == 'GET':
        return render(request, 'core/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # Faz a autenticação do usuário
        if (user is not None) and (user.is_active): # Se existir usuário cadastrado e ele for ativo
            auth_login(request, user) # Faz o login do usuário
            desired_datetime = localtime().strftime('%Y-%m-%d %H:%M:%S')
            HistoricoAcesso.objects.create(idUser=user.id, user=request.user, dataLogon=desired_datetime)
            return redirect('dashboard')
        else:
            contexto = {'flag': False, 'msg': 'Email e Senha não correspondem', 'username': username, 'password': password}
            return render(request, "core/login.html", contexto)


def dashboard(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                user = request.user
                print(user)
                usuario = Usuario.objects.get(user=user)
                nomeCompleto = usuario.nomeCompleto

                # request.session['imageUser'] = "/static/media/" + str(usuario.imagemPerfil)

            except Exception as e: # Caso ocorra erros na consulta
                if request.user.is_authenticated:
                    auth_logout(request)
                    contexto = {'flag': False, 'msg': e}
                    return render(request, "core/login.html", contexto)
            return render(request, "core/dashboard.html")
        else:
            return redirect('login')

def logout(request):
    print("Saindo")
    auth_logout(request)
    return redirect('login')

#####################################################################