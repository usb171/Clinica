// Seleciona o item de menu //////////////////
$('#id_list_menu_agenda').addClass('active');
// Seleciona o item de menu //////////////////

var dataSelectFullcalendar;
var calendar = null;

function getDataCorrente(){
    diaSistema = $("#id_dataHora a").text().split('/')[0].split(' ')[0];
    mesSistema = $("#id_dataHora a").text().split('/')[1].split(' ')[0];
    anoSistema = $("#id_dataHora a").text().split('/')[2].split(' ')[0];
    dataCorrente = diaSistema + "/" + mesSistema + "/" + anoSistema;
    return {'diaSistema':diaSistema, 'mesSistema':mesSistema, 'anoSistema':anoSistema, 'dataCorrente':dataCorrente}
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

    var calendarEl = document.getElementById('calendar');
    calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['interaction', 'dayGrid', 'timeGrid', 'list' ],
        themeSystem: 'bootstrap',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
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

        select: function(date, jsEvent, view) {
            $("#id_modal_form_calendario").modal('show');
            var date = formatDate(date.startStr, 'pt-br');
            dateSelectFullcalendar = date;
            $('.modal-title').text(date);
            $('.timepicker').val('');
            $("#id_paciente").val("").trigger('change');
            $("#id_servico").val("").trigger('change');
            $("#id_profissional").val("").trigger('change');
            $("#id_hora_inicio").val("")
            $("#id_hora_fim").val("")
            $('#id_data').val(date);
            $("#id_agenda").val("-1");
            $("#id_paciente_id").val("-1");
            $("#id_profissional_id").val("-1");
            validarCampos();
        },

        eventClick: function(info) {

            $.ajax({
                url: "/agenda/buscarAgendaAjax",
                data: {'id_agenda': info.event.id},
                dataType: 'json',
                success: function (data) {
                    agenda = data.agenda;
                    $("#id_modal_form_calendario").modal('show');
                    $('.modal-title').text(formatDate(agenda.dataInicio.split('T')[0], 'pt-br'));
                    $("#id_hora_inicio").val(agenda.horaInicio);
                    $("#id_hora_fim").val(agenda.horaFim);

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
            for(i = 0 ; i < data.agenda.length; i++){
                evento = data.agenda[i];
                calendar.addEvent({
                    id: evento.id,
                    title: evento.titulo,
                    start: evento.dataInicio,
                    end : evento.dataFim,
                    textColor:"White"
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




