from django.shortcuts import render, HttpResponse, redirect
from usuario.models import Usuario
from servico.models import Servico
from django.http import JsonResponse

import json

def servico(request):

    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        if request.method == 'GET':
            contexto = {
                'servicos': Servico.objects.filter(clinica=clinica)
            }
            return render(request, 'servico/servicos.html', contexto)
        elif request.method == 'POST':
            for key in request.POST.keys():
                print(key, " ", request.POST[key])

            ativo = request.POST['ativo']
            nome = request.POST['nome']
            preco = request.POST['preco']
            tempo = request.POST['tempo']
            prazoRetorno = request.POST['prazoRetorno']
            prazoValidade = request.POST['prazoValidade']

            nomeDocumento1 = request.POST['nomeDocumento_1']
            codeDocumento1 = request.POST['codeDocumento_1']

            nomeDocumento2 = request.POST['nomeDocumento_2']
            codeDocumento2 = request.POST['codeDocumento_2']

            nomeDocumento3 = request.POST['nomeDocumento_3']
            codeDocumento3 = request.POST['codeDocumento_3']

            nomeDocumento4 = request.POST['nomeDocumento_4']
            codeDocumento4 = request.POST['codeDocumento_4']

            id_servico = request.POST['id_servico']

            if Servico.objects.filter(id=id_servico).exists():  # Caso exista o ID passado, edite esse Serviço
                servico_obj = Servico.objects.filter(id=id_servico)
                servico_obj.update(nome=nome,
                                    preco=preco,
                                    tempo=tempo,
                                    ativo=ativo,
                                    clinica=clinica,
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
                'nomeDocumento_1':servico.nomeDocumento1,
                'nomeDocumento_2':servico.nomeDocumento2,
                'nomeDocumento_3':servico.nomeDocumento3,
                'nomeDocumento_4':servico.nomeDocumento4,
                'codeDocumento_1': servico.codeDocumento1,
                'codeDocumento_2': servico.codeDocumento2,
                'codeDocumento_3': servico.codeDocumento3,
                'codeDocumento_4': servico.codeDocumento4,
               }
        return JsonResponse(data)
    else:
        return redirect('login')
