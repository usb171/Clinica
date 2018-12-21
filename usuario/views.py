from django.shortcuts import render
from usuario.models import Usuario
from django.http import HttpResponse
import json


def usuarios(request):
    if request.method == 'GET':
        contexto = {'usuarios': Usuario.objects.all()}
        print(contexto)
        return render(request, 'usuario/usuarios.html', contexto)

def novoUsuario(request):
    print(request.POST)
    return HttpResponse(json.dumps({'ok': True, 'msg': "Usuário Salvo com Sucesso!"}), content_type="application/json")
