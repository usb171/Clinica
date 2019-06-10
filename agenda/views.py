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

            dict_dados['dataFim'] = dict_dados['data']+"T"+dict_dados['horaFim']
            dict_dados['dataInicio'] = dict_dados['data']+"T"+dict_dados['horaInicio']
            dict_dados['profissional'] = Usuario.objects.get(id=id_profissional)
            dict_dados['paciente'] = Paciente.objects.get(id=id_paciente)
            dict_dados['titulo'] = dict_dados['paciente'].nomeCompleto

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
        clinica_obj = Usuario.objects.get(user=request.user)
        agenda_obj = Agenda.objects.filter(clinica=clinica_obj.clinica, id=id_agenda)
        agenda = list(agenda_obj.values('titulo', 'paciente', 'profissional', 'servico', 'horaInicio', 'horaFim', 'dataInicio', 'dataFim'))[0]
        id_usuario = agenda['profissional']
        json = {'agenda': agenda}

        try:
            usuario_obj = Usuario.objects.get(clinica=clinica_obj.clinica, id=id_usuario, ativo="ON")
            json['agenda']['profissional_id'] = usuario_obj.id
            json['agenda']['profissional'] = usuario_obj.nomeCompleto
        except:
            json['agenda']['profissional_id'] = ''
            json['agenda']['profissional'] = ''

        try:
            id_paciente = agenda['paciente']
            paciente_obj = Paciente.objects.get(clinica=clinica_obj.clinica, id=id_paciente, ativo="ON")
            json['agenda']['paciente_id'] = paciente_obj.id
            json['agenda']['paciente'] = paciente_obj.nomeCompleto
            json['agenda']['paciente_telefone'] = paciente_obj.telefone
        except:
            json['agenda']['paciente_id'] = ''
            json['agenda']['paciente'] = ''
            json['agenda']['paciente_telefone'] = ''

        try:
            servicos = Servico.objects.filter(clinica=clinica_obj.clinica, id__in=agenda['servico'].split(','), ativo="ON")
            json['agenda']['servicos'] = list(servicos.values('id', 'nome'))
        except:
            json['agenda']['servicos'] = []

        return JsonResponse(json)

    else:
        return redirect('login')