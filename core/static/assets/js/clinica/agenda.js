// Seleciona o item de menu //////////////////
$('#id_list_menu_agenda').addClass('active');
// Seleciona o item de menu //////////////////

var dataSelectFullcalendar;
var calendar = null;
var eventosAgenda = {};

function getDataCorrente(){
    diaSistema = $("#id_dataHora a").text().split('/')[0].split(' ')[0];
    mesSistema = $("#id_dataHora a").text().split('/')[1].split(' ')[0];
    anoSistema = $("#id_dataHora a").text().split('/')[2].split(' ')[0];
    tempoCorrente = $("#id_dataHora a").text().split(' ')[2]
    dataCorrente = diaSistema + "/" + mesSistema + "/" + anoSistema;
    return {'diaSistema':diaSistema, 'mesSistema':mesSistema, 'anoSistema':anoSistema, 'dataCorrente':dataCorrente, 'tempoCorrente': tempoCorrente}
}

$("#id_data").mask("99/99/9999", {placeholder: "__/__/____", onKeyPress: function(data, e, field, options){
    var dia = data.split('/')[0], mes = data.split('/')[1], ano = data.split('/')[2]

    if(data.length >= 2)
        if(dia > 31)
            $("#id_data").val('31/');
        else if(dia == 0)
            $("#id_data").val('01/');
    else
        if(data.length >=5)
            if(mes > 12)
                $("#id_data").val(dia+'/12/');
            else if(mes == 0)
                $("#id_data").val(dia+'/01/');
            else if(mes == 2 && dia > 28)
                $("#id_data").val('28/02');

    if(data.length == 10){

        dataSistema = getDataCorrente()

        diaSistema = dataSistema.diaSistema;
        mesSistema = dataSistema.mesSistema;
        anoSistema = dataSistema.anoSistema;

        dataCorrente = dataSistema.dataCorrente;

        if(ano == 0){
            $("#id_data").val(dia+'/'+mes+'/'+anoSistema);
            ano=anoSistema;
        }

        validarCampos();

    }
    else if(data.length){
        $("#id_data").removeClass("is-valid").addClass("is-invalid");
        $("#id_data")[0].setCustomValidity("Data inválida");
    }


}});

// Converte a dataString en para pt-br
function formatDate(data, formato) {
  if (formato == 'pt-br') {
    return (data.substr(0, 10).split('-').reverse().join('/'));
  } else {
    return (data.substr(0, 10).split('/').reverse().join('-'));
  }
}

//*********************************************** Calendário ***********************************************************
document.addEventListener('DOMContentLoaded', function() {

    var flag = false;

    var calendarEl = document.getElementById('calendar');
    calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['interaction', 'dayGrid', 'timeGrid', 'list'],
        themeSystem: 'bootstrap',
        header: {
            left: 'prev,next,today agendar',
            center: 'title',
            right: 'listDay,dayGridMonth'
            //right: 'dayGridMonth,timeGridWeek,timeGridDay,listDay'
        },
        defaultDate: new Date(),
        locale: 'pt-br',
        buttonIcons: false, // show the prev/next text
        weekNumbers: false,
        navLinks: true, // can click day/week names to navigate views
        businessHours: true, // display business hours
        editable: false,
        selectable: true,
        slotDuration: '00:05:00',
        minTime: '08:00:00',
        maxTime: '18:00:00',
        defaultView: 'list',

        select: function(date, jsEvent, view) {
            $("#id_modal_form_calendario").modal('show');
            var date = formatDate(date.startStr, 'pt-br');
            dateSelectFullcalendar = date;
            $('.modal-title').text(date);
            $('.timepicker').val('');
            $("#id_descricao").val("");
            $("#id_paciente").val("").trigger('change');
            $("#id_servico").empty().trigger("change");
            $("#id_profissional").val("").trigger('change');
            $("#id_hora_inicio").val("");
            $("#id_hora_fim").val("");
            $("#id_hora_chegada").val("");
            $("#id_hora_atendimento").val("");
            $('#id_data').val(date);
            $("#id_agenda").val("-1");
            $("#id_paciente_id").val("-1");
            $("#id_profissional_id").val("-1");
            $("#id_descricao").val("");
            $('#id_bt_agendado').click();
            validarCampos();
        },
        eventClick: function(info) {

            $.ajax({
                url: "/agenda/buscarAgendaAjax",
                data: {'id_agenda': info.event.id},
                dataType: 'json',
                success: function (data) {
                    agenda = data.agenda;
                    $("#id_servico").empty().trigger("change");

                    $("#id_modal_form_calendario").modal('show');
                    $('.modal-title').text(formatDate(agenda.dataInicio.split('T')[0], 'pt-br'));
                    $("#id_hora_inicio").val(agenda.horaInicio);
                    $("#id_hora_fim").val(agenda.horaFim);

                    $("#id_descricao").val(agenda.descricao);

                    status = agenda.status;
                    resetBtnStatus();
                    if(status == "AGENDADO")
                        $('#id_bt_agendado').attr('class', 'btn btn-primary');
                    else if (status == "CONFIRMADO")
                        $('#id_bt_confirmado').attr('class', 'btn btn-primary');
                    else if (status == "AGUARDANDO")
                        $('#id_bt_aguardando').attr('class', 'btn btn-primary');
//                      $('#id_bt_aguardando').trigger('click', {data: agenda.horaChegada});
                    else if (status == "EM ATENDIMENTO")
                        $('#id_bt_em_atendimento').attr('class', 'btn btn-primary');
//                      $('#id_bt_em_atendimento').trigger('click', {data: agenda.horaAtendimento});
                    else if (status == "ATENDIDO")
                        $('#id_bt_atendido').attr('class', 'btn btn-primary');
                    else if (status == "NAO ATENDIMENTO")
                        $('#id_bt_nao_atendido').attr('class', 'btn btn-primary');


                    var pacienteOption = new Option(agenda.paciente, agenda.paciente_id, true, true);
                    var profissionalOption = new Option(agenda.profissional, agenda.profissional_id, true, true);

                    for( i = 0; i < agenda.servicos.length; i++){
                        var servicoOption = new Option(agenda.servicos[i].nome, agenda.servicos[i].id, true, true);
                        $("#id_servico").append(servicoOption).trigger('change');
                    }

                    $("#id_paciente").append(pacienteOption).trigger('change');
                    $("#id_profissional").append(profissionalOption).trigger('change');

                    $("#id_servico").val(agenda.servico.split(",")).trigger('change');
                    $("#id_data").val(formatDate(agenda.dataInicio.split('T')[0], 'pt-br'))
                    $("#id_agenda").val(info.event.id);
                    validarCampos();

                }
            })
        },
        events: [],
        customButtons: {
            agendar: {
                text: 'Agendar',
                click: function() {
                    $("#id_modal_form_calendario").modal('show');
                    $('.modal-title').text('__/__/__');
                    $('.timepicker').val('');
                    $("#id_paciente").val("").trigger('change');
                    $("#id_servico").val("").trigger('change');
                    $("#id_profissional").val("").trigger('change');
                    $("#id_hora_inicio").val("");
                    $("#id_hora_chegada").val("");
                    $("#id_hora_atendimento").val("");
                    $("#id_hora_fim").val("");
                    $('#id_data').val('');
                    $("#id_agenda").val("-1");
                    $("#id_paciente_id").val("-1");
                    $("#id_profissional_id").val("-1");
                    $("#id_descricao").val("");
                    $('#id_bt_agendado').click();

                }
            }
        },

        eventPositioned: function(event){

            el = event['el'];
            className = el.className

            if(className == 'fc-list-item'){

                publicId = event['event']._def.publicId; // ID do evento da Agenda

                // Cabeçalho da lista ///////////////////////////////////////////////////////////////////////////////////////////////////////////
                $('.fc-list-heading').html(
                    '<td class="fc-widget-header" style="border: 1px solid #dddddd;"><a class="fc-list-heading-main">Agendado</a></td>' +
                    '<td class="fc-widget-header" style="border: 1px solid #dddddd; width:15%;"><a class="fc-list-heading-main">Status</a></td>' +
                    '<td class="fc-widget-header" style="border: 1px solid #dddddd;"><a class="fc-list-heading-main">Paciente</a></td>' +
                    '<td class="fc-widget-header" style="border: 1px solid #dddddd;"><a class="fc-list-heading-main">Profissional</a></td>' +
                    '<td class="fc-widget-header" style="border: 1px solid #dddddd;width:2%"><a class="fc-list-heading-main">Chegada</a></td>' +
                    '<td class="fc-widget-header" style="border: 1px solid #dddddd;width:2%"><a class="fc-list-heading-main">Atendido</a></td>'
                );
                // Cabeçalho da lista ///////////////////////////////////////////////////////////////////////////////////////////////////////////

                // Add de grid nas linhas padrão /////////////////////////////////
                $(el.cells[0]).attr('style', 'border: 1px solid #dddddd;');
                $(el.cells[1]).attr('style', 'border: 1px solid #dddddd;');
                $(el.cells[2]).attr('style', 'border: 1px solid #dddddd;');
                // Add de grid nas linhas padrão /////////////////////////////////

                el.insertCell(); // Cria uma nova célula na linha, coluna profissional
                el.insertCell(); // Cria uma nova célula na linha, coluna chegada
                el.insertCell(); // Cria uma nova célula na linha, coluna atendimento

                evento = eventosAgenda.agenda.filter(x => x.id === parseInt(publicId))[0]; // Buscado o evento pelo ID do evento

                $(el.cells[1].firstChild).attr('class', '').text(evento.status); // Atualiza o nome do status
                // Atualiza a célula com o nome de pacientes
                $(el.cells[3]).attr('class', 'fc-list-item-title fc-widget-content')
                              .attr('style', 'border: 1px solid #dddddd;')
                              .append("<a>"+evento.profissional__nomeCompleto+"</a>");

                // Atualiza a célula com o tempo de chegada
                $(el.cells[4]).attr('class', 'fc-list-item-title fc-widget-content')
                              .attr('style', 'border: 1px solid #dddddd;')
                              .append("<a>"+evento.horaChegada+"</a>");

                // Atualiza a célula com o tempo de chegada
                $(el.cells[5]).attr('class', 'fc-list-item-title fc-widget-content')
                              .attr('style', 'border: 1px solid #dddddd;')
                              .append("<a>"+evento.horaAtendimento+"</a>");


            }

        },
    });

    calendar.render();




});

//Carrega os eventos do calendário
var parent = $(".be-loading");
if( parent.length ){
    parent.addClass('be-loading-active');
    $.ajax({
        url: "/agenda/carregarAgendaAjax",
        dataType: 'json',
        success: function (data) {
            eventosAgenda = data;
            for(i = 0 ; i < data.agenda.length; i++){
                evento = data.agenda[i];
                calendar.addEvent({
                    id: evento.id,
                    title: evento.titulo,
                    start: evento.dataInicio,
                    end : evento.dataFim,
                    textColor:"White",
                })
            }

            $.ajax({
                url: "/core/getDataHoraAjax",
                dataType: 'json',
                success: function (data) {
                    if(data.dataHora){
                        setTimeout(function(){
                            parent.removeClass('be-loading-active');
                        }, 100);
                    }
                }
            })
        }
    })
}

//*********************************************** Field Hora ***********************************************************

function validarCampos(){

    $("#id_hora_inicio").removeClass("is-valid").removeClass("is-invalid");
    $("#id_hora_fim").removeClass("is-valid").removeClass("is-invalid");
    $("#id_data").removeClass("is-invalid").removeClass("is-invalid");
    $("#id_hora_inicio")[0].setCustomValidity('');
    $("#id_hora_fim")[0].setCustomValidity('');
    $("#id_data")[0].setCustomValidity('');


    dataSistema = getDataCorrente()

    // Valida a data
    if(formatDate($("#id_data").val()) >= formatDate(dataSistema.dataCorrente)){
        if(!$('#id_data').hasClass('is-valid')){
            $.gritter.add({
                title: 'Agenda - Data',
                text: 'Data Válida',
                class_name: 'color success'
            });
        }
        $("#id_data").removeClass("is-invalid").addClass("is-valid");
        $("#id_data")[0].setCustomValidity('');
        $('.modal-title').text($("#id_data").val());
    }
    else{
        $("#id_data").removeClass("is-valid").addClass("is-invalid")
        $("#id_data")[0].setCustomValidity("A data não pode ser menor do que a data corrente");
        $.gritter.add({
            title: 'Agenda - Data',
            text: 'A data não pode ser menor do que a data corrente',
            class_name: 'color danger'
        });
        return false;
    }

    // Validar horário
    var final = $("#id_hora_fim").val()
    var inicial = $("#id_hora_inicio").val()

    if( inicial < final && inicial.length){
        $('#id_hora_inicio').addClass("is-valid");
        $("#id_hora_fim").addClass("is-valid");
        $.gritter.add({
            title: 'Agenda - Horário',
            text: 'Horário Válido',
            class_name: 'color success'
        });
    }
    else{
        $('#id_hora_inicio').addClass("is-invalid");
        $('#id_hora_fim').addClass("is-invalid");
        if( inicial == final ){
            $('#id_hora_inicio')[0].setCustomValidity("Os horários inicial e final são iguais");
            $('#id_hora_fim')[0].setCustomValidity("Os horários inicial e final são iguais");
            $.gritter.add({
                title: 'Agenda - Horário',
                text: 'Os horários inicial e final são iguais',
                class_name: 'color danger'
            });

            return false;

        }else if( final < inicial ){
            $('#id_hora_fim')[0].setCustomValidity("O horário final é menor do que o inicial");
            $.gritter.add({
                title: 'Agenda - Horário',
                text: 'O horário final é menor do que o inicial',
                class_name: 'color danger'
            });

            return false;
        }

    }

    return true;
}

function atualizarHoraFinal(){
    ids = [];
    servicos = $('#id_servico').select2('data');
    for( i = 0; i < servicos.length; i++){
        ids.push(servicos[i].id);
    }

    if(ids.length){
        $.ajax({
        url: "/servico/buscarInformacaoGeralServicoAjax",
        data: {'ids': ids.toString()},
        dataType: 'json',
        success: function (data) {
            var somaTempoServicos = 0;
            var tempoString = '';

            for(i = 0 ; i < data.servicos.length; i++){
                servico = data.servicos[i];
                somaTempoServicos += parseInt(servico.tempo);
            }

            var tempoInicial = $("#id_hora_inicio").val();
            var tempoInicial_minutos =  parseInt(tempoInicial.split(':')[0]) * 60 + parseInt(tempoInicial.split(':')[1]);

            var totalDeMinutos = tempoInicial_minutos + somaTempoServicos;

            var hora = Math.floor(totalDeMinutos / 60);
            var minuto = totalDeMinutos % 60;
            if(hora.toString().length == 1) tempoString += '0' + hora + ':';
            else tempoString += hora + ':';
            if(minuto.toString().length == 1) tempoString += '0' + minuto;
            else tempoString += minuto;
            $('#id_hora_fim').val(tempoString);

        }
    });
    }else{
        $('#id_hora_fim').val('');
    }
}

$("#id_profissional").select2({
  ajax: {
    url: "/usuario/buscarDadosUsuario2Ajax",
    dataType: 'json',
    delay: 100,
    data: function (params) {
      return {
        q: params.term,
      };
    },
    processResults:function(data){
        return {
            results: $.map(data.usuario, function (usuario) {
                return {
                    id: usuario.id,
                    text: usuario.nomeCompleto,
                    email: usuario.email,
                }
            })
        };
    }
  },
  width: '100%',
  language: 'pt-BR',
  escapeMarkup: function (markup) { return markup; },
  templateResult: formatSelect2ProfissionalResult,
  templateSelection: formatSelect2ProfissionalSelection
});

$("#id_paciente").select2({
  ajax: {
    url: "/paciente/buscarDadosPaciente2Ajax",
    dataType: 'json',
    delay: 100,
    data: function (params) {
      return {
        q: params.term,
      };
    },
    processResults:function(data){
        return {
            results: $.map(data.paciente, function (paciente) {
                return {
                    id: paciente.id,
                    text: paciente.nomeCompleto,
                    telefone: paciente.telefone,
                }
            })
        };
    }
  },
  width: '100%',
  language: 'pt-BR',
  escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
  templateResult: formatSelect2PacienteResult,
  templateSelection: formatSelect2PacienteSelection
});

$("#id_servico").select2({
  ajax: {
    url: "/servico/buscarDadosServico2Ajax",
    dataType: 'json',
    delay: 100,
    data: function (params) {
      return {
        q: params.term,
      };
    },
    processResults:function(data){
        return {
            results: $.map(data.servico, function (servico) {
                return {
                    id: servico.id,
                    text: servico.nome,
                    tempo: servico.tempo,
                    preco: servico.preco
                }
            })
        };
    }
  },
  width: '100%',
  language: 'pt-BR',
  escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
  templateResult: formatSelect2ServicoResult,
  templateSelection: formatSelect2ServicoSelection
});

function formatSelect2ProfissionalResult(usuario){
    if (usuario.loading) {return usuario.text;}
    return "<div>" +
                "<div>" + usuario.text + " </div>" +
                "<div>" + usuario.email + "</div>" +
           "</div>";
}

function formatSelect2PacienteResult(paciente){
    if (paciente.loading) {return paciente.text;}
    return "<div>" +
                "<div>" + paciente.text + " </div>" +
                "<div>" + paciente.telefone + "</div>" +
           "</div>";
}

function formatSelect2ServicoResult(servico){
    if (servico.loading) {return servico.text;}
    return "<div>" +
                "<div>" + servico.text + " </div>" +
                "<div>" + servico.tempo + " Minutos </div>" +
                "<div>" + servico.preco + " </div>" +
           "</div>";
}

function formatSelect2ProfissionalSelection(usuario){return usuario.text;}

function formatSelect2PacienteSelection(paciente){return paciente.text;}

function formatSelect2ServicoSelection(servico){return servico.text;}



$('#id_servico').on('select2:select', function (e) {
    atualizarHoraFinal();
    validarCampos();
});

$('#id_servico').on('select2:unselect', function (e) {
    atualizarHoraFinal();
    validarCampos();
});



// Formulários /////////////////////////////////////
$('#id_form_novo_evento').submit(function(e){

    $("#id_button_modal").prop("disabled",true);
    $("#id_data").val( formatDate($('.modal-title').text()));
    $("#id_servico_input").val($("#id_servico").select2("val"));
    $("#id_paciente_id").val($('#id_paciente').select2('val'));
    $("#id_profissional_id").val($('#id_profissional').select2('val'));

    validarCampos();

    e.preventDefault();
    $.post("/agenda/", $(this).serialize(), function(data){
        if (data.ok){
            console.log("Novo Evento Salvo Com Sucesso!");
            $("#id_button_modal").prop("disabled",false);
            window.location.reload()
        }else{
            console.log(data.msg);
            $("#id_button_modal").prop("disabled",false);
        }
    }, 'json');
});
// Formulários ////////////////////////////////////








/// Formulário Cadastro Rápido Paciente ///////////////////////////////////////////////////////////////////////////

$("#id_telefone").mask("(99) 9999-9999");
$("#id_celular").mask("(99) 99999-9999");
$("#id_nomeCompleto").keyup(function(event){$("#id_nomeCompleto").val(($('#id_nomeCompleto').val()).toUpperCase());});

$("#id_cpf").mask("000.000.000-00").keyup(function(event){
  var strCPF = $(this).val().replace(/\D+/g,'');/*console.log(strCPF)*/;var Soma;var Resto;Soma = 0;if (strCPF == "00000000000"){
  $("#id_cpf").removeClass("is-valid").addClass("is-invalid"); $(this)[0].setCustomValidity('CPF Inválido'); return;}
  for (i=1; i<=9; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);Resto = (Soma * 10) % 11;
  if ((Resto == 10) || (Resto == 11))  Resto = 0;if (Resto != parseInt(strCPF.substring(9, 10)) ){
  $("#id_cpf").removeClass("is-valid").addClass("is-invalid"); $(this)[0].setCustomValidity('CPF Inválido');
  if(!strCPF.length){$("#id_cpf").removeClass("is-invalid"); $(this)[0].setCustomValidity('');}  return;} Soma = 0;
  for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);Resto = (Soma * 10) % 11;
  if ((Resto == 10) || (Resto == 11))  Resto = 0;if (Resto != parseInt(strCPF.substring(10, 11) ) ){
  $("#id_cpf").removeClass("is-valid").addClass("is-invalid"); $(this)[0].setCustomValidity('CPF Inválido'); return;}
  else{$("#id_cpf").removeClass("is-invalid").addClass("is-valid"); $(this)[0].setCustomValidity('');}
});
function validarData(id, campo){
    $(id).mask("99/99/9999", {placeholder: "__/__/____", onKeyPress: function(data, e, field, options){
        var dia = data.split('/')[0], mes = data.split('/')[1], ano = data.split('/')[2]
        //console.log(data + " " + id);
        $("#id_idade").val("");
        if(data.length >= 2)
            if(dia > 31)
                $(id).val('31/');
            else if(dia == 0)
                $(id).val('01/');
        else
            if(data.length >=5)
                if(mes > 12)
                    $(id).val(dia+'/12/');
                else if(mes == 0)
                    $(id).val(dia+'/01/');
                else if(mes == 2 && dia > 28)
                    $(id).val('28/02');

        if(data.length == 10){

            diaSistema = $("#id_dataHora a").text().split('/')[0].split(' ')[0];
            mesSistema = $("#id_dataHora a").text().split('/')[1].split(' ')[0];
            anoSistema = $("#id_dataHora a").text().split('/')[2].split(' ')[0];

            if(ano == 0){ $(id).val(dia+'/'+mes+'/'+anoSistema); ano=anoSistema;}

            if(campo == "dataNascimento"){
                if(ano >= 1930 && ano <= anoSistema){
                    $(id).removeClass("is-invalid").addClass("is-valid");
                    $("#id_idade").removeClass("is-invalid").addClass("is-valid");
                    $(id)[0].setCustomValidity('');
                    if(diaSistema >= dia && mesSistema >= mes)
                        $("#id_idade").val(anoSistema-ano + " anos");
                    else
                        if(ano == anoSistema)
                            $("#id_idade").val("0 anos");
                        else
                            $("#id_idade").val((anoSistema-ano)-1 + " anos");
                }
                else{
                    $(id).removeClass("is-valid").addClass("is-invalid")
                    if(ano < 1930){
                        $(id)[0].setCustomValidity("Data de nascimento muito antiga");
                    }
                    else{
                        $(id)[0].setCustomValidity("Data de nascimento não pode ser maior do que o ano corrente");
                    }
                }
            } else if(campo == "convenioValidade"){

                var dataCampo = new Date(mes+'/'+dia+'/'+ano).setHours(0,0,0,0);
                var dataSistema = new Date(mesSistema+'/'+diaSistema+'/'+anoSistema).setHours(0,0,0,0);

                if (dataCampo < dataSistema) {
                  $(id).removeClass("is-valid").addClass("is-invalid");
                  $(id)[0].setCustomValidity("Convênio expirado");
                }else{
                  $(id).removeClass("is-invalid").addClass("is-valid");
                  $(id)[0].setCustomValidity("");
                }
            }

        }
        else if(data.length){
            $(id).removeClass("is-valid").addClass("is-invalid");
//          $("#id_idade").removeClass("is-valid").addClass("is-invalid");
            $(id)[0].setCustomValidity("Data inválida");
        }
    }
    });
}
validarData("#id_dataNascimento", "dataNascimento");

$('#id_modal_form_novo_paciente').on('shown.bs.modal', function () {
    $("#id_modal_form_calendario").attr('hidden', 'true');
    $('#id_modal_title').text('Cadastro Rápido de Pacientes');
    $('#id_modal_form_novo_paciente form').trigger("reset"); // reseta todos os campos do formulário
})

$('#id_modal_form_novo_paciente').on('hide.bs.modal', function () {
    $("#id_modal_form_calendario").removeAttr('hidden');
})

$('#id_form_novo_paciente').submit(function(e){

    $("button").prop("disabled",true);

    e.preventDefault();
    $.post("/paciente/meusPacientes", $(this).serialize(), function(data){
        if (data.ok){
            console.log("Novo Paciente Salvo Com Sucesso!");
            $("button").prop("disabled",false);
             $.gritter.add({
                title: 'Paciente',
                text: 'Paciente Salvo com Sucesso',
                class_name: 'color success'
            });
            var pacienteOption = new Option(data.paciente.nomeCompleto, data.paciente.id, true, true);
            $("#id_paciente").append(pacienteOption).trigger('change');
            $("#id_modal_form_novo_paciente").attr('hidden', 'true');
            $("#id_modal_form_calendario").removeAttr('hidden');

        }else{
            console.log(data.msg);
            $("button").prop("disabled",false);
            $.gritter.add({
                title: 'Paciente',
                text: 'Erro ao Salvar o Paciente',
                class_name: 'color danger'
            });
        }
    }, 'json');
});

/// Formulário Cadastro Rápido Paciente ///////////////////////////////////////////////////////////////////////////









function resetBtnStatus(){
    $('#id_bt_agendado').attr('class', 'btn btn-secondary');
    $('#id_bt_confirmado').attr('class', 'btn btn-secondary');
    $('#id_bt_aguardando').attr('class', 'btn btn-secondary');
    $('#id_bt_em_atendimento').attr('class', 'btn btn-secondary');
    $('#id_bt_atendido').attr('class', 'btn btn-secondary');
    $('#id_bt_nao_atendido').attr('class', 'btn btn-secondary');
}

// Butões do status /////////////////////////////
$('#id_bt_agendado').on('click', function () {
    resetBtnStatus();
    $(this).attr('class', 'btn btn-primary');
    $("#id_status").val('AGENDADO');
    $("#id_hora_chegada").val("");
    $("#id_hora_atendimento").val("");
})

$('#id_bt_confirmado').on('click', function () {
    resetBtnStatus();
    $(this).attr('class', 'btn btn-primary');
    $("#id_status").val('CONFIRMADO');
    $("#id_hora_chegada").val("");
    $("#id_hora_atendimento").val("");
})

$('#id_bt_aguardando').on('click', function (event, data) {
    resetBtnStatus();
    $(this).attr('class', 'btn btn-primary');
    $("#id_status").val('AGUARDANDO');
    $("#id_hora_chegada").val(getDataCorrente().tempoCorrente);
    $("#id_hora_atendimento").val("");

})

$('#id_bt_em_atendimento').on('click', function (event, data) {
    resetBtnStatus();
    $(this).attr('class', 'btn btn-primary')
    $("#id_status").val('EM ATENDIMENTO');
    $("#id_hora_atendimento").val(getDataCorrente().tempoCorrente);
})

$('#id_bt_atendido').on('click', function () {
 resetBtnStatus();
    $(this).attr('class', 'btn btn-primary');
    $("#id_status").val('ATENDIDO');
})

$('#id_bt_nao_atendido').on('click', function () {
    resetBtnStatus();
    $(this).attr('class', 'btn btn-primary');
    $("#id_status").val('NAO ATENDIDO');
    $("#id_hora_atendimento").val("");
})

