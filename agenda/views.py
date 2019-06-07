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
        usuarios = Usuario.objects.filter(clinica=clinica)

        if request.method == 'GET':
            contexto = {
                'clinicas': clinica,
                'servicos': servicos,
                'pacientes': pacientes,
                'profissionais': usuarios,
            }
            return render(request, 'agenda/agenda.html', contexto)
        elif request.method == 'POST':
            dict_dados = {'clinica': clinica}
            for key in request.POST.keys():
                dict_dados[key] = request.POST[key]
                print(key, " ", dict_dados[key])
            del dict_dados['csrfmiddlewaretoken']

            id_agenda = dict_dados.pop('id_agenda')  # Remove e pega o id da agenda
            id_paciente = dict_dados.pop('id_paciente')  # Remove e pega o id do paciente
            id_profissional = dict_dados.pop('id_profissional')  # Remove e pega o id do profissional

            dict_dados['titulo'] = dict_dados['paciente']
            dict_dados['dataFim'] = dict_dados['data']+"T"+dict_dados['horaFim']
            dict_dados['dataInicio'] = dict_dados['data']+"T"+dict_dados['horaInicio']
            dict_dados['profissional'] = Usuario.objects.get(id=id_profissional)
            dict_dados['paciente'] = Paciente.objects.get(id=id_paciente)

            if Agenda.objects.filter(id=id_agenda).exists():  # Caso exista o ID passado, edite esse agenda
                agenda_obj = Agenda.objects.filter(id=id_agenda)
                agenda_obj.update(**dict_dados)
            else:
                agenda_obj = Agenda.objects.create(**dict_dados)
                agenda_obj.save()

            return HttpResponse(json.dumps({'ok': True, 'msg': "Evento Salvo com Sucesso!", 'erros': {}}),
                                content_type="application/json")
    else:
        return redirect('login')


def carregarAgendaAjax(request):
    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        agenda = list(Agenda.objects.filter(clinica=clinica).values('id', 'titulo', 'dataInicio', 'dataFim'))
        return JsonResponse({'agenda': agenda})
    else:
        return redirect('login')


def buscarAgendaAjax(request):
    if request.user.is_authenticated:
        id_agenda = request.GET.get('id_agenda', None)
        clinica = Usuario.objects.get(user=request.user).clinica
        agenda = list(Agenda.objects.filter(clinica=clinica, id=id_agenda).values('titulo', 'paciente', 'profissional', 'servico', 'horaInicio', 'horaFim', 'dataInicio', 'dataFim'))[0]
        json = {'agenda': agenda}

        json['agenda']['paciente'] = Paciente.objects.get(id=json['agenda']['paciente']).nomeCompleto
        json['agenda']['profissional'] = Usuario.objects.get(id=json['agenda']['profissional']).nomeCompleto

        return JsonResponse(json)
    else:
        return redirect('login')