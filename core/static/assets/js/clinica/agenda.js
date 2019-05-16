// Seleciona o item de menu //////////////////
$('#id_list_menu_agenda').addClass('active');
// Seleciona o item de menu //////////////////


var dataSelectFullcalendar;
var calendar = null;


// Converte a dataString en para pt-br
function formatDate(data, formato) {
  if (formato == 'pt-br') {
    return (data.substr(0, 10).split('-').reverse().join('/'));
  } else {
    return (data.substr(0, 10).split('/').reverse().join('-'));
  }
}

//*********************************************** Field Hora ***********************************************************
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
        editable: true,
        selectable: true,
        select: function(date, jsEvent, view) {
            $("#id_modal_form_calendario").modal('show');
            var date = formatDate(date.startStr, 'pt-br');
            dateSelectFullcalendar = date;
            $('.modal-title').text(date);
            $('.timepicker').val('');
            $("#id_hora_inicio").removeClass("is-valid").removeClass("is-invalid");
            $("#id_hora_fim").removeClass("is-valid").removeClass("is-invalid");
            $("#id_hora_inicio")[0].setCustomValidity('');
            $("#id_hora_fim")[0].setCustomValidity('');
            $("#id_paciente").val("").trigger('change');
            $("#id_servico").val("").trigger('change');
        },

        eventClick: function(info) {

            $("#id_modal_form_calendario").modal('show');
            $.ajax({
                url: "/agenda/buscarAgendaAjax",
                data: {'id_agenda': info.event.id},
                dataType: 'json',
                success: function (data) {
                    dateStart = data.agenda.dateStart
                    dateEnd = data.agenda.dateEnd
                    $('.modal-title').text(formatDate(dateStart.split('T')[0], 'pt-br'));
                    $("#id_hora_inicio").val(dateStart.split('T')[1])
                    $("#id_hora_fim").val(dateEnd.split('T')[1])
                    $("#id_paciente").val(data.agenda.paciente).trigger('change');
                    $("#id_servico").val(data.agenda.servico.split(",")).trigger('change');
                    $("#id_agenda").val(info.event.id);
                }
            })

        },

        events: [],

    });
    calendar.render();
});

$(".timepicker").datetimepicker({
    format: 'hh:ii',
    minuteStep: 15,
    weekStart: 1,
    todayBtn:  false,
    autoclose: true,
    todayHighlight: true,
    startView: 1,
    minView: 0,
    maxView: 1,
    forceParse: 0,
});

$(".datetimepicker").find('thead th').remove();
$(".datetimepicker").find('thead').append($('<th class="switch">').text('Hora'));
$('.switch').css('width','190px');

$("#id_hora_inicio").on("change", function (e) {
    var inicial = $(this).val()
    var final = $("#id_hora_fim").val()

    if(final == "") return;

    if( inicial < final ){
        $(this).removeClass("is-invalid").addClass("is-valid");
        $("#id_hora_fim").removeClass("is-invalid").addClass("is-valid");
        $(this)[0].setCustomValidity('');
    }
    else if( inicial == final ){
        $(this).removeClass("is-valid").addClass("is-invalid");
        $("#id_hora_inicio").removeClass("is-valid").addClass("is-invalid");
        $(this)[0].setCustomValidity("A data final é igual a inicial");
        $.gritter.add({
            title: 'Agenda',
            text: 'A data final é igual a inicial',
            class_name: 'color danger'
        });
    }
    else{
        console.log("erro")
        $(this).removeClass("is-valid").addClass("is-invalid");
        $("#id_hora_fim").removeClass("is-valid").addClass("is-invalid");
        $(this)[0].setCustomValidity("A data inicial é maior que a final");
        $.gritter.add({
            title: 'Agenda',
            text: 'A data inicial é maior que a final',
            class_name: 'color danger'
        });
    }
});
$("#id_hora_fim").on("change", function (e) {
    var final = $(this).val()
    var inicial = $("#id_hora_inicio").val()

    if(inicial == "") return;

    if( inicial < final ){
        $(this).removeClass("is-invalid").addClass("is-valid");
        $("#id_hora_inicio").removeClass("is-invalid").addClass("is-valid");
        $(this)[0].setCustomValidity('');
    }
    else if( inicial == final ){
        $(this).removeClass("is-valid").addClass("is-invalid");
        $("#id_hora_inicio").removeClass("is-valid").addClass("is-invalid");
        $(this)[0].setCustomValidity("A data final é igual a inicial");
        $.gritter.add({
            title: 'Agenda',
            text: 'A data final é igual a inicial',
            class_name: 'color danger'
        });
    }
    else{
        $(this).removeClass("is-valid").addClass("is-invalid");
        $("#id_hora_inicio").removeClass("is-valid").addClass("is-invalid");
        $(this)[0].setCustomValidity("A data final é menor que a inicial");
        $.gritter.add({
            title: 'Agenda',
            text: 'A data final é menor que a inicial',
            class_name: 'color danger'
        });
    }
});
//*********************************************** Field Hora ***********************************************************

$('.select2').select2({
    width: '100%',
});


//Carrega os eventos do calendário
$.ajax({
    url: "/agenda/carregarAgendaAjax",
    dataType: 'json',
    success: function (data) {
      for(i = 0 ; i < data.agenda.length; i++){
        evento = data.agenda[i];
        calendar.addEvent({
            id: evento.id,
            title: evento.titulo,
            start: evento.dateStart,
            end : evento.dateEnd,
            //color: 'green'
            textColor:"White"
        })
      }
    }
})

// Formulários /////////////////////////////////////
$('#id_form_novo_evento').submit(function(e){

    $("#id_button_modal").prop("disabled",true);
    $("#id_data").val( formatDate($('.modal-title').text()));
    $("#id_servico_input").val($("#id_servico").select2("val"));


    e.preventDefault();
    $.post("/agenda/agenda", $(this).serialize(), function(data){
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