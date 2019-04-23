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
                'grupoConvenio': paciente.grupoConvenio,
                'grupoFamiliar': paciente.grupoFamiliar,
                'dataNascimento': paciente.dataNascimento,
                'convenio1': paciente.convenio1,
                'convenio2': paciente.convenio2,
                'convenio3': paciente.convenio3,
                'convenio4': paciente.convenio4,
                'numeroCarteira1': paciente.numeroCarteira1,
                'numeroCarteira2': paciente.numeroCarteira2,
                'numeroCarteira3': paciente.numeroCarteira3,
                'numeroCarteira4': paciente.numeroCarteira4,
                'convenioValidade1': paciente.convenioValidade1,
                'convenioValidade2': paciente.convenioValidade2,
                'convenioValidade3': paciente.convenioValidade3,
                'convenioValidade4': paciente.convenioValidade4,
                'grau1': paciente.grau1,
                'grau2': paciente.grau2,
                'grau3': paciente.grau3,
                'grau4': paciente.grau4,
                'nomeFamiliar1': paciente.nomeFamiliar1,
                'nomeFamiliar2': paciente.nomeFamiliar2,
                'nomeFamiliar3': paciente.nomeFamiliar3,
                'nomeFamiliar4': paciente.nomeFamiliar4,
               }
        return JsonResponse(data)
    else:
        return redirect('login')

def paciente(request):

    if request.user.is_authenticated:
        clinica = Usuario.objects.get(user=request.user).clinica
        #path_paciente_clinica = 'core/static/media/paciente/' + str(clinica.id)
        #if not os.path.isdir(path_paciente_clinica):
            #os.mkdir(path_paciente_clinica)

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
            #print(form.errors)
            if form.is_valid():

                dados = form.cleaned_data

                #fotoPerfil = dados['fotoPerfil'],
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
                grupoConvenio = dados['grupoConvenio']
                grupoFamiliar = dados['grupoFamiliar']
                dataNascimento = dados['dataNascimento']
                convenio1 = dados['convenio1']
                convenio2 = dados['convenio2']
                convenio3 = dados['convenio3']
                convenio4 = dados['convenio4']
                numeroCarteira1 = dados['numeroCarteira1']
                numeroCarteira2 = dados['numeroCarteira2']
                numeroCarteira3 = dados['numeroCarteira3']
                numeroCarteira4 = dados['numeroCarteira4']
                convenioValidade1 = dados['convenioValidade1']
                convenioValidade2 = dados['convenioValidade2']
                convenioValidade3 = dados['convenioValidade3']
                convenioValidade4 = dados['convenioValidade4']

                grau1 = dados['grau1']
                grau2 = dados['grau2']
                grau3 = dados['grau3']
                grau4 = dados['grau4']
                nomeFamiliar1 = dados['nomeFamiliar1']
                nomeFamiliar2 = dados['nomeFamiliar2']
                nomeFamiliar3 = dados['nomeFamiliar3']
                nomeFamiliar4 = dados['nomeFamiliar4']

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
                                        grupoConvenio=grupoConvenio,
                                        grupoFamiliar=grupoFamiliar,
                                        dataNascimento=dataNascimento,
                                        convenio1=convenio1,
                                        convenio2=convenio2,
                                        convenio3=convenio3,
                                        convenio4=convenio4,
                                        numeroCarteira1=numeroCarteira1,
                                        numeroCarteira2=numeroCarteira2,
                                        numeroCarteira3=numeroCarteira3,
                                        numeroCarteira4=numeroCarteira4,
                                        convenioValidade1=convenioValidade1,
                                        convenioValidade2=convenioValidade2,
                                        convenioValidade3=convenioValidade3,
                                        convenioValidade4=convenioValidade4,
                                        grau1=grau1,
                                        grau2=grau2,
                                        grau3=grau3,
                                        grau4=grau4,
                                        nomeFamiliar1=nomeFamiliar1,
                                        nomeFamiliar2=nomeFamiliar2,
                                        nomeFamiliar3=nomeFamiliar3,
                                        nomeFamiliar4=nomeFamiliar4,
                                        )

                    #filename = path_paciente_clinica + "/" + str(id_paciente) + '.jpg'

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
                                            grupoConvenio=grupoConvenio,
                                            grupoFamiliar=grupoFamiliar,
                                            dataNascimento=dataNascimento,
                                            convenio1=convenio1,
                                            convenio2=convenio2,
                                            convenio3=convenio3,
                                            convenio4=convenio4,
                                            numeroCarteira1=numeroCarteira1,
                                            numeroCarteira2=numeroCarteira2,
                                            numeroCarteira3=numeroCarteira3,
                                            numeroCarteira4=numeroCarteira4,
                                            convenioValidade1=convenioValidade1,
                                            convenioValidade2=convenioValidade2,
                                            convenioValidade3=convenioValidade3,
                                            convenioValidade4=convenioValidade4,
                                            grau1=grau1,
                                            grau2=grau2,
                                            grau3=grau3,
                                            grau4=grau4,
                                            nomeFamiliar1=nomeFamiliar1,
                                            nomeFamiliar2=nomeFamiliar2,
                                            nomeFamiliar3=nomeFamiliar3,
                                            nomeFamiliar4=nomeFamiliar4,
                                            )
                    paciente_obj.save()

                return HttpResponse(json.dumps({'ok': True, 'msg': "Paciente Salvo com Sucesso!", 'erros': {}}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'ok': False, 'msg': "Ocorreu um Erro ao Criar um Novo Usuário!", 'erros': {}}), content_type="application/json")
    else:
        return redirect('login')
