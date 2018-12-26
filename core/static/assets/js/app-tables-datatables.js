/*!
 * Beagle v1.5.2
 * https://foxythemes.net
 *
 * Copyright (c) 2018 Foxy Themes
 */

var App = (function () {
  'use strict';

  App.dataTables = function( ){

    //We use this to apply style to certain elements
    $.fn.DataTable.ext.pager.numbers_length = 4;
    $.extend( true, $.fn.dataTable.defaults, {
      dom:
        "<'row be-datatable-header'<'col-sm-6'l><'col-sm-6'f>>" +
        "<'row be-datatable-body'<'col-sm-12'tr>>" +
        "<'row be-datatable-footer'<'col-sm-5'i><'col-sm-7'p>>"
    } );

//    $("#id_table_novoUsuario").dataTable({
//
//        "bSearch": true,
//        "bLengthChange": false,
//        "pageLength": 10,
//        "paging":   true,
//        "responsive": true,
//        "ordering": true,
//        "info":     true,
//
//        "language": {
//        "sEmptyTable": "Nenhum registro encontrado",
//        "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
//        "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
//        "sInfoFiltered": "(Filtrados de _MAX_ registros)",
//        "sInfoPostFix": "",
//        "sInfoThousands": ".",
//        "sLengthMenu": "_MENU_ resultados por página",
//        "sLoadingRecords": "Carregando...",
//        "sProcessing": "Processando...",
//        "sZeroRecords": "Nenhum registro encontrado",
//        "sSearch": "Pesquisar",
//        "oPaginate": {
//            "sNext": "Próximo",
//            "sPrevious": "Anterior",
//            "sFirst": "Primeiro",
//            "sLast": "Último"
//        },
//        "oAria": {
//            "sSortAscending": ": Ordenar colunas de forma ascendente",
//            "sSortDescending": ": Ordenar colunas de forma descendente"
//        }
//        },

//        buttons: [
//            {
//                text: 'My button',
//                action: function ( e, dt, node, config ) {
//                    alert( 'Button activated' );
//                }
//            }
//        ]
//
//
//    });

//    $("#id_table_modal_novoUsuario").dataTable({
//
//        "bSearch": true,
//        "bLengthChange": false,
//        "pageLength": 5,
//        "paging":   true,
//        "responsive": true,
//        "ordering": true,
//        "info":     true,
//
//        "language": {
//        "sEmptyTable": "Nenhum registro encontrado",
//        "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
//        "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
//        "sInfoFiltered": "(Filtrados de _MAX_ registros)",
//        "sInfoPostFix": "",
//        "sInfoThousands": ".",
//        "sLengthMenu": "_MENU_ resultados por página",
//        "sLoadingRecords": "Carregando...",
//        "sProcessing": "Processando...",
//        "sZeroRecords": "Nenhum registro encontrado",
//        "sSearch": "Pesquisar",
//        "oPaginate": {
//            "sNext": "Próximo",
//            "sPrevious": "Anterior",
//            "sFirst": "Primeiro",
//            "sLast": "Último"
//        },
//        "oAria": {
//            "sSortAscending": ": Ordenar colunas de forma ascendente",
//            "sSortDescending": ": Ordenar colunas de forma descendente"
//        }
//        },
//
//
//
//
//    });

    //Remove search & paging dropdown
    $("#table2").dataTable({
      pageLength: 6,
      dom:  "<'row be-datatable-body'<'col-sm-12'tr>>" +
            "<'row be-datatable-footer'<'col-sm-5'i><'col-sm-7'p>>"
    });

    //Enable toolbar button functions
    $("#table3").dataTable({
      buttons: [
        'copy', 'csv', 'excel', 'pdf', 'print'
      ],
      "lengthMenu": [[6, 10, 25, 50, -1], [6, 10, 25, 50, "All"]],
      dom:  "<'row be-datatable-header'<'col-sm-6'l><'col-sm-6 text-right'B>>" +
            "<'row be-datatable-body'<'col-sm-12'tr>>" +
            "<'row be-datatable-footer'<'col-sm-5'i><'col-sm-7'p>>"
    });

    $("#table4").dataTable({
      responsive: true
    });

    $("#table5").dataTable({
      responsive: {
        details: {
          display: $.fn.dataTable.Responsive.display.childRowImmediate,
          type: ''
        }
      }
    });

    $("#table6").dataTable({
      responsive: {
        details: {
          display: $.fn.dataTable.Responsive.display.modal ({
            header: function (row) {
              var data = row.data();
              return 'Details';
            }
          }),
          renderer: $.fn.dataTable.Responsive.renderer.tableAll ({
            tableClass: 'table'
          })
        }
      }
    });
  };

  return App;
})(App || {});
