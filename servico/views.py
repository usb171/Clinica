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
            # for key in request.POST.keys():
            #     print(key, " ", request.POST[key])

            ativo = request.POST['ativo']
            nome = request.POST['nome']
            preco = request.POST['preco']
            tempo = request.POST['tempo']

            rateio1 = request.POST['rateio_1']
            rateio2 = request.POST['rateio_2']
            rateio3 = request.POST['rateio_3']
            rateio4 = request.POST['rateio_4']
            rateio5 = request.POST['rateio_5']
            rateio6 = request.POST['rateio_6']

            tipoRateio1 = request.POST['tipoRateio_1']
            tipoRateio2 = request.POST['tipoRateio_2']
            tipoRateio3 = request.POST['tipoRateio_3']
            tipoRateio4 = request.POST['tipoRateio_4']
            tipoRateio5 = request.POST['tipoRateio_5']
            tipoRateio6 = request.POST['tipoRateio_6']

            titulo1 = request.POST['titulo_1']
            titulo2 = request.POST['titulo_2']
            titulo3 = request.POST['titulo_3']
            titulo4 = request.POST['titulo_4']
            titulo5 = request.POST['titulo_5']
            titulo6 = request.POST['titulo_6']


            prazoRetorno = request.POST['prazoRetorno']
            prazoValidade = request.POST['prazoValidade']

            nomeDocumento1 = request.POST['nomeDocumento_1']
            nomeDocumento2 = request.POST['nomeDocumento_2']
            nomeDocumento3 = request.POST['nomeDocumento_3']
            nomeDocumento4 = request.POST['nomeDocumento_4']
            nomeDocumento5 = request.POST['nomeDocumento_5']
            nomeDocumento6 = request.POST['nomeDocumento_6']

            codeDocumento1 = request.POST['codeDocumento_1']
            codeDocumento2 = request.POST['codeDocumento_2']
            codeDocumento3 = request.POST['codeDocumento_3']
            codeDocumento4 = request.POST['codeDocumento_4']
            codeDocumento5 = request.POST['codeDocumento_5']
            codeDocumento6 = request.POST['codeDocumento_6']

            id_servico = request.POST['id_servico']

            if Servico.objects.filter(id=id_servico).exists():  # Caso exista o ID passado, edite esse Serviço
                servico_obj = Servico.objects.filter(id=id_servico)
                servico_obj.update(nome=nome,
                                   preco=preco,
                                   tempo=tempo,
                                   ativo=ativo,
                                   clinica=clinica,
                                   rateio1=rateio1,
                                   rateio2=rateio2,
                                   rateio3=rateio3,
                                   rateio4=rateio4,
                                   rateio5=rateio5,
                                   rateio6=rateio6,
                                   titulo1=titulo1,
                                   titulo2=titulo2,
                                   titulo3=titulo3,
                                   titulo4=titulo4,
                                   titulo5=titulo5,
                                   titulo6=titulo6,
                                   tipoRateio1=tipoRateio1,
                                   tipoRateio2=tipoRateio2,
                                   tipoRateio3=tipoRateio3,
                                   tipoRateio4=tipoRateio4,
                                   tipoRateio5=tipoRateio5,
                                   tipoRateio6=tipoRateio6,
                                   prazoRetorno=prazoRetorno,
                                   prazoValidade=prazoValidade,
                                   nomeDocumento1=nomeDocumento1,
                                   codeDocumento1=codeDocumento1,
                                   nomeDocumento2=nomeDocumento2,
                                   codeDocumento2=codeDocumento2,
                                   nomeDocumento3=nomeDocumento3,
                                   codeDocumento3=codeDocumento3,
                                   nomeDocumento4=nomeDocumento4,
                                   codeDocumento4=codeDocumento4,
                                   )
            else:  # Crie um Serviço
                servico_obj = Servico.objects.create(nome=nome,
                                   preco=preco,
                                   tempo=tempo,
                                   ativo=ativo,
                                   clinica=clinica,
                                   rateio1=rateio1,
                                   rateio2=rateio2,
                                   rateio3=rateio3,
                                   rateio4=rateio4,
                                   rateio5=rateio5,
                                   rateio6=rateio6,
                                   titulo1=titulo1,
                                   titulo2=titulo2,
                                   titulo3=titulo3,
                                   titulo4=titulo4,
                                   titulo5=titulo5,
                                   titulo6=titulo6,
                                   tipoRateio1=tipoRateio1,
                                   tipoRateio2=tipoRateio2,
                                   tipoRateio3=tipoRateio3,
                                   tipoRateio4=tipoRateio4,
                                   tipoRateio5=tipoRateio5,
                                   tipoRateio6=tipoRateio6,
                                   prazoRetorno=prazoRetorno,
                                   prazoValidade=prazoValidade,
                                   nomeDocumento1=nomeDocumento1,
                                   codeDocumento1=codeDocumento1,
                                   nomeDocumento2=nomeDocumento2,
                                   codeDocumento2=codeDocumento2,
                                   nomeDocumento3=nomeDocumento3,
                                   codeDocumento3=codeDocumento3,
                                   nomeDocumento4=nomeDocumento4,
                                   codeDocumento4=codeDocumento4,
                                                     )
                servico_obj.save()

            return HttpResponse(json.dumps({'ok': True, 'msg': "Serviço Salvo com Sucesso!", 'erros': {}}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Serviço!", 'erros': {}}), content_type="application/json")
    else:
        return redirect('login')

def buscarDadosServicoAjax(request):
    if request.user.is_authenticated:
        try:
            servico = Servico.objects.get(id=request.GET.get('id_servico', None))
        except:
            return redirect('login')
        data = {
                'ativo': servico.ativo,
                'nome': servico.nome,
                'tempo': servico.tempo,
                'preco': servico.preco,
                'id_servico': servico.pk,

                'prazoRetorno': servico.prazoRetorno,
                'prazoValidade': servico.prazoValidade,

                'nomeDocumento_1': servico.nomeDocumento1,
                'nomeDocumento_2': servico.nomeDocumento2,
                'nomeDocumento_3': servico.nomeDocumento3,
                'nomeDocumento_4': servico.nomeDocumento4,
                'nomeDocumento_5': servico.nomeDocumento5,
                'nomeDocumento_6': servico.nomeDocumento6,

                'codeDocumento_1': servico.codeDocumento1,
                'codeDocumento_2': servico.codeDocumento2,
                'codeDocumento_3': servico.codeDocumento3,
                'codeDocumento_4': servico.codeDocumento4,
                'codeDocumento_5': servico.codeDocumento5,
                'codeDocumento_6': servico.codeDocumento6,

                'rateio_1': servico.rateio1,
                'rateio_2': servico.rateio2,
                'rateio_3': servico.rateio3,
                'rateio_4': servico.rateio4,
                'rateio_5': servico.rateio5,
                'rateio_6': servico.rateio6,

                'tipoRateio_1': servico.tipoRateio1,
                'tipoRateio_2': servico.tipoRateio2,
                'tipoRateio_3': servico.tipoRateio3,
                'tipoRateio_4': servico.tipoRateio4,
                'tipoRateio_5': servico.tipoRateio5,
                'tipoRateio_6': servico.tipoRateio6,

                'titulo_1': servico.titulo1,
                'titulo_2': servico.titulo2,
                'titulo_3': servico.titulo3,
                'titulo_4': servico.titulo4,
                'titulo_5': servico.titulo5,
                'titulo_6': servico.titulo6,

        }
        return JsonResponse(data)
    else:
        return redirect('login')
