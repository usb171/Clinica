from django.shortcuts import render, HttpResponse, redirect
from usuario.models import Usuario
from servico.models import Servico
from core.models import Titulo
from django.http import JsonResponse

import json

def servico(request):

    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        if request.method == 'GET':
            contexto = {
                'servicos': Servico.objects.filter(clinica=clinica),
                'titulos': Titulo.objects.filter(clinica=clinica)
            }
            return render(request, 'servico/servicos.html', contexto)
        elif request.method == 'POST':
            dict_dados = {'clinica': clinica}
            for key in request.POST.keys():
                dict_dados[key] = request.POST[key]
            del dict_dados['csrfmiddlewaretoken']

            id_servico = dict_dados.pop('id_servico') # Remove e pega o id do serviço

            if Servico.objects.filter(id=id_servico).exists():  # Caso exista o ID passado, edite esse Serviço
                servico_obj = Servico.objects.filter(id=id_servico)
                servico_obj.update(**dict_dados)
            else:  # Crie um Serviço
                servico_obj = Servico.objects.create(**dict_dados)
                servico_obj.save()

            return HttpResponse(json.dumps({'ok': True, 'msg': "Serviço Salvo com Sucesso!", 'erros': {}}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Serviço!", 'erros': {}}), content_type="application/json")
    else:
        return redirect('login')

def buscarInformacaoGeralServicoAjax(request):
    if request.user.is_authenticated:
        try:
            ids = request.GET.get('ids', None).split(',')
            clinica = Usuario.objects.get(user=request.user).clinica
            servicos = list(Servico.objects.filter(clinica=clinica, id__in=ids).values('id', 'ativo', 'nome', 'tempo'))
        except:
            return redirect('login')

        json = {'servicos': servicos}

        return JsonResponse(json)
    else:
        return redirect('login')

def buscarDadosServicoAjax(request):
    if request.user.is_authenticated:
        try:
            clinica = Usuario.objects.get(user=request.user).clinica
            servico = Servico.objects.get(clinica=clinica, id=request.GET.get('id_servico', None))
        except:
            return redirect('login')
        data = {
                'ativo': servico.ativo,
                'nome': servico.nome,
                'tempo': servico.tempo,
                'preco': servico.preco,
                'id_servico': servico.pk,
                'quantSessao': servico.quantSessao,
                'prazoRetorno': servico.prazoRetorno,
                'prazoValidade': servico.prazoValidade,
                'nomeDocumento_1': servico.nomeDocumento_1,
                'nomeDocumento_2': servico.nomeDocumento_2,
                'nomeDocumento_3': servico.nomeDocumento_3,
                'nomeDocumento_4': servico.nomeDocumento_4,
                'nomeDocumento_5': servico.nomeDocumento_5,
                'nomeDocumento_6': servico.nomeDocumento_6,
                'codeDocumento_1': servico.codeDocumento_1,
                'codeDocumento_2': servico.codeDocumento_2,
                'codeDocumento_3': servico.codeDocumento_3,
                'codeDocumento_4': servico.codeDocumento_4,
                'codeDocumento_5': servico.codeDocumento_5,
                'codeDocumento_6': servico.codeDocumento_6,
                'rateio_1': servico.rateio_1,
                'rateio_2': servico.rateio_2,
                'rateio_3': servico.rateio_3,
                'rateio_4': servico.rateio_4,
                'rateio_5': servico.rateio_5,
                'rateio_6': servico.rateio_6,
                'tipoRateio_1': servico.tipoRateio_1,
                'tipoRateio_2': servico.tipoRateio_2,
                'tipoRateio_3': servico.tipoRateio_3,
                'tipoRateio_4': servico.tipoRateio_4,
                'tipoRateio_5': servico.tipoRateio_5,
                'tipoRateio_6': servico.tipoRateio_6,
                'titulo_1': servico.titulo_1,
                'titulo_2': servico.titulo_2,
                'titulo_3': servico.titulo_3,
                'titulo_4': servico.titulo_4,
                'titulo_5': servico.titulo_5,
                'titulo_6': servico.titulo_6,
        }
        return JsonResponse(data)
    else:
        return redirect('login')

def buscarDadosServico2Ajax(request):
    if request.user.is_authenticated:
        json = {'servico': []}
        try:
            q = request.GET.get('q', None)
            clinica = Usuario.objects.get(user=request.user).clinica
            if q:
                servico = Servico.objects.filter(nome__contains=q, ativo='ON', clinica=clinica).order_by('nome')
                json['servico'] = list(servico.values('id', 'nome', 'tempo', 'preco'))
                return JsonResponse(json)
            else:
                servico = Servico.objects.filter(ativo='ON', clinica=clinica).order_by('nome')[:10]
                json['servico'] = list(servico.values('id', 'nome', 'tempo', 'preco'))
                return JsonResponse(json)

        except Exception as e:
            print(e)
            return JsonResponse(json)
    else:
        return redirect('login')