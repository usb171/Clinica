
var App = (function () {
  'use strict';
  
  App.pageCalendar = function( ){
    $(".datetimepicker").datetimepicker({
      language: 'pt-BR',
      autoclose: true,
    });
    $(".timepicker").mask("00:00");

    $('.services').select2({
      width: '90%',
      minimumInputLength: 3,
      tags: true,
      ajax: {
        url: 'http://bebeppy.local:8000/usuario/servicos.json',
        dataType: 'json',
        processResults: function (data) {
          return { results: data }
        }
      }
    });

    $('.clientes').select2({
      width: '90%',
      minimumInputLength: 3,
      ajax: {
        url: 'http://bebeppy.local:8000/usuario/autocomplete.json',
        dataType: 'json',
        processResults: function (data) {
          return { results: data }
        }
      }
    });
    /* initialize the external events
    -----------------------------------------------------------------*/
    $('#external-events .fc-event').each(function() {
      // store data so the calendar knows to render an event upon drop
      $(this).data('event', {
        title: $.trim($(this).text()), // use the element's text as the event title
        stick: true // maintain when user navigates (see docs on the renderEvent method)
      });

      // make the event draggable using jQuery UI
      $(this).draggable({
        zIndex: 999,
        revert: true,      // will cause the event to go back to its
        revertDuration: 0  //  original position after the drag
      });

    });


    /* initialize the calendar
    -----------------------------------------------------------------*/
    let calendar = $('#calendar');
    let events = [];

    calendar.fullCalendar({
      lang: 'pt-br',
      header: {
        left: 'title',
        center: '',
        right: 'month,agendaWeek,agendaDay, today, prev,next',
      },
      defaultDate: new Date(),
      selectable: true,
      editable: true,
      eventLimit: true,
      droppable: true,
      events: events,
      dayClick: function(date, jsEvent, view){
        $("#schedule_date").val(date.format("DD/MM/YYYY"));
        $("#form-success").niftyModal();
      },
      select: function(startDate, endDate, jsEvent, view, resource) {
        $("#schedule_start").val(startDate.format("HH:mm"));
        $("#schedule_end").val(endDate.format("HH:mm"));
      },
      drop: function() {
        if ($('#drop-remove').is(':checked')) {
          $(this).remove();
        }
      },
    });

  };

  return App;
})(App || {});
