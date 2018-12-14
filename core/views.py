from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from usuario.models import Usuario
from django.shortcuts import redirect
from .models import UsuarioLogado, HistoricoAcesso
from django.utils.timezone import localtime
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver



def login(request):

    if request.method == 'GET':
        return render(request, 'core/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # Faz a autenticação do usuário
        if (user is not None) and (user.is_active): # Se existir usuário cadastrado e ele for ativo
            auth_login(request, user) # Faz o login do usuário
            request.session.set_expiry(3600) # Finaliza a sessão em X segundos
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

                request.session['imageUser'] = "/static/media/" + str(usuario.imagemPerfil)

            except Exception as e: # Caso ocorra erros na consulta
                if request.user.is_authenticated:
                    auth_logout(request)
                    contexto = {'flag': False, 'msg': e}
                    return render(request, "core/login.html", contexto)

            return render(request, "core/dashboard.html")
        else:
            return redirect('login')



#Sinais utilizados para criar instâncias de login e logout no sistema

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    UsuarioLogado.objects.get_or_create(user=kwargs.get('user'))
    desired_datetime = localtime().strftime('%Y-%m-%d %H:%M:%S')
    HistoricoAcesso.objects.create(idUser=kwargs.get('user').id, user=request.user, dataLogon=desired_datetime)


@receiver(user_logged_out)
def logout(sender, **kwargs):
    UsuarioLogado.objects.filter(user=kwargs.get('user')).delete()

#####################################################################