from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from usuario.models import Usuario

from paciente.models import Paciente
from core.models import Convenio, Origem, ControleCampo
from .forms import PacienteForm
from django.shortcuts import redirect
import base64
import os.path

import json


def buscarEmailAjax(request):
    if request.user.is_authenticated:
        email = request.GET.get('email', None)
        email_original = request.GET.get('email_original', None)
        if email_original == email:
            data = {'email': False}
        else:
            data = {'email': Paciente.objects.filter(email=request.GET.get('email', None)).exists()}
        return JsonResponse(data)
    else:
        return redirect('login')

def buscarDadosPacienteAjax(request):
    if request.user.is_authenticated:
        try:
            paciente = Paciente.objects.get(id=request.GET.get('id_paciente', None))
            clinica = Usuario.objects.get(user=request.user).clinica
            image_path = 'core/static/media/paciente/' + str(clinica.id) + '/' + str(paciente.id) + '.jpg'
        except:
            return redirect('login')

        data = {
                'cpf': paciente.cpf,
                'cep': paciente.cep,
                'rua': paciente.rua,
                'sexo': paciente.sexo,
                'email': paciente.email,
                'ativo': paciente.ativo,
                'idade': paciente.idade,
                'numero': paciente.numero,
                'origem': paciente.origem,
                'quadra': paciente.quadra,
                'bairro': paciente.bairro,
                'cidade': paciente.cidade,
                'estado': paciente.estado,
                'id_paciente': paciente.pk,
                'celular': paciente.celular,
                'telefone': paciente.telefone,
                'profissao': paciente.profissao,
                'observacao': paciente.observacao,
                'complemento': paciente.complemento,
                'estadoCivil': paciente.estadoCivil,
                'nomeCompleto': paciente.nomeCompleto,
                #'nomeFamiliar': paciente.nomeFamiliar,
                'grupoConvenio': paciente.grupoConvenio,
                'grupoFamiliar': paciente.grupoFamiliar,
                'dataNascimento': paciente.dataNascimento,
                #'grauParentesco': paciente.grauParentesco,
                'image_path': image_path,
               }
        return JsonResponse(data)
    else:
        return redirect('login')

def paciente(request):

    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        path_paciente_clinica = 'core/static/media/paciente/' + str(clinica.id)
        if not os.path.isdir(path_paciente_clinica):
            os.mkdir(path_paciente_clinica)

        if request.method == 'GET':
            contexto = {
                'pacientes': Paciente.objects.filter(clinica=clinica),
                'convenios': Convenio.objects.filter(clinica=clinica),
                'origens': Origem.objects.filter(clinica=clinica),
                'controleCampo': ControleCampo.objects.filter(clinica=clinica)[0]
            }
            return render(request, 'paciente/pacientes.html', contexto)
        elif request.method == 'POST':

            #for key in request.POST.keys():
                #print(key, " ", request.POST[key])


            form = PacienteForm(request.POST)
            print(form.errors)
            if form.is_valid():
                dados = form.cleaned_data
                cpf = dados['cpf']
                cep = dados['cep']
                rua = dados['rua']
                sexo = dados['sexo']
                ativo = dados['ativo']
                idade = dados['idade']
                email = dados['email']
                numero = dados['numero']
                origem = dados['origem']
                quadra = dados['quadra']
                bairro = dados['bairro']
                cidade = dados['cidade']
                estado = dados['estado']
                celular = dados['celular']
                telefone = dados['telefone']
                profissao = dados['profissao']
                observacao = dados['observacao']
                complemento = dados['complemento']
                estadoCivil = dados['estadoCivil']
                nomeCompleto = dados['nomeCompleto']
                #nomeFamiliar = dados['nomeFamiliar']
                grupoConvenio = dados['grupoConvenio']
                grupoFamiliar = dados['grupoFamiliar']
                dataNascimento = dados['dataNascimento']
                #grauParentesco = dados['grauParentesco']


                id_paciente = request.POST['id_paciente']

                if Paciente.objects.filter(id=id_paciente).exists(): # Caso exista o ID passado, edite esse Paciente
                    paciente_obj = Paciente.objects.filter(id=id_paciente)
                    paciente_obj.update(cpf=cpf,
                                        cep=cep,
                                        rua=rua,
                                        sexo=sexo,
                                        email=email,
                                        idade=idade,
                                        ativo=ativo,
                                        numero=numero,
                                        origem=origem,
                                        quadra=quadra,
                                        bairro=bairro,
                                        cidade=cidade,
                                        estado=estado,
                                        celular=celular,
                                        telefone=telefone,
                                        profissao=profissao,
                                        observacao=observacao,
                                        complemento=complemento,
                                        estadoCivil=estadoCivil,
                                        nomeCompleto=nomeCompleto,
                                        #nomeFamiliar=nomeFamiliar,
                                        grupoConvenio=grupoConvenio,
                                        grupoFamiliar=grupoFamiliar,
                                        dataNascimento=dataNascimento,
                                        #grauParentesco=grauParentesco,
                                        )

                    filename = path_paciente_clinica + "/" + str(id_paciente) + '.jpg'

                else: #Crie um Paciente
                    paciente_obj = Paciente.objects.create(cpf=cpf,
                                            cep=cep,
                                            rua=rua,
                                            sexo=sexo,
                                            email=email,
                                            idade=idade,
                                            ativo=ativo,
                                            numero=numero,
                                            origem=origem,
                                            quadra=quadra,
                                            bairro=bairro,
                                            cidade=cidade,
                                            estado=estado,
                                            celular=celular,
                                            clinica=clinica,
                                            telefone=telefone,
                                            profissao=profissao,
                                            observacao=observacao,
                                            complemento=complemento,
                                            estadoCivil=estadoCivil,
                                            nomeCompleto=nomeCompleto,
                                            #nomeFamiliar=nomeFamiliar,
                                            grupoConvenio=grupoConvenio,
                                            grupoFamiliar=grupoFamiliar,
                                            #grauParentesco=grauParentesco,
                                            dataNascimento=dataNascimento)
                    paciente_obj.save()
                    filename = path_paciente_clinica + "/" + str(paciente_obj.id) + '.jpg'

                imgdata = base64.b64decode(str(request.POST['imagem_paciente']).split(",")[1])
                with open(filename, 'wb') as f:
                    f.write(imgdata)

                return HttpResponse(json.dumps({'ok': True, 'msg': "Paciente Salvo com Sucesso!", 'erros': {}}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Usuário!", 'erros': {}}), content_type="application/json")
    else:
        return redirect('login')


