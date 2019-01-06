from django.shortcuts import render
from paciente.models import Paciente


def paciente(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            contexto = {'pacientes': Paciente.objects.all()}
            print(contexto)
            return render(request, 'paciente/pacientes.html', contexto)
        elif request.method == 'POST':
            pass
    else:
        pass
