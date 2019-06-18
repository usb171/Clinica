from django.shortcuts import render
from usuario.models import Usuario
from paciente.models import Paciente
from servico.models import Servico
from agenda.models import Agenda
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

import json


def agenda(request):
    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        pacientes = Paciente.objects.filter(clinica=clinica)
        servicos = Servico.objects.filter(clinica=clinica)

        if request.method == 'GET':
            contexto = {
                'clinicas': clinica,
                'servicos': servicos,
                'pacientes': pacientes,
            }
            return render(request, 'agenda/agenda.html', contexto)
        elif request.method == 'POST':
            # for key in request.POST.keys():
            #     print(key, " ", request.POST[key])

            data = request.POST['data']
            hora_inicio = request.POST['hora_inicio']
            hora_fim = request.POST['hora_fim']
            paciente = request.POST['paciente']
            servico = request.POST['servico']

            id_agenda = request.POST['id_agenda']

            if Agenda.objects.filter(id=id_agenda).exists():  # Caso exista o ID passado, edite esse agenda
                agenda_obj = Agenda.objects.filter(id=id_agenda)
                agenda_obj.update(
                    clinica=clinica,
                    titulo=paciente,
                    paciente=paciente,
                    servico=servico,
                    dataFim=data+"T"+hora_fim,
                    dataInicio=data+"T"+hora_inicio,
                )
            else:
                agenda_obj = Agenda.objects.create(
                    clinica=clinica,
                    titulo=paciente,
                    paciente=paciente,
                    servico=servico,
                    dataFim=data+"T"+hora_fim,
                    dataInicio=data+"T"+hora_inicio,
                )

                agenda_obj.save()

            return HttpResponse(json.dumps({'ok': True, 'msg': "Evento Salvo com Sucesso!", 'erros': {}}),
                                content_type="application/json")
    else:
        return redirect('login')


def carregarAgendaAjax(request):
    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        agenda = Agenda.objects.filter(clinica=clinica)

        json = {'agenda': []}

        for evento in agenda:
            json['agenda'].append({'id': evento.id, 'titulo': evento.titulo, 'dateStart': evento.dataInicio, 'dateEnd': evento.dataFim})

        return JsonResponse(json)
    else:
        return redirect('login')



def buscarAgendaAjax(request):
    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        agenda = Agenda.objects.get(clinica=clinica, id=request.GET.get('id_agenda', None))
        json = {'agenda': {'titulo': agenda.titulo, 'paciente': agenda.paciente, 'servico': agenda.servico,'dateStart': agenda.dataInicio, 'dateEnd': agenda.dataFim}}
        return JsonResponse(json)
    else:
        return redirect('login')