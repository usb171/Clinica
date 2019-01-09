from django.shortcuts import render, HttpResponse
from paciente.models import Paciente
from core.models import Convenio
import json


def paciente(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            contexto = {
                'pacientes': Paciente.objects.all(),
                'convenios': Convenio.objects.all(),
            }
            print(contexto)
            return render(request, 'paciente/pacientes.html', contexto)
        elif request.method == 'POST':
            for key in request.POST.keys():
                print(key, " ", request.POST[key])
            return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Usuário!", 'erros': {}}), content_type="application/json")

    else:
        pass
