
// Seleciona o item de menu //////////////////
$('#id_list_menu_configuracao').addClass('active');
$('#id_item_titulo').addClass('active');
// Seleciona o item de menu //////////////////

// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////
$("#id_nomeTitulo").keyup(function(event){$("#id_nomeTitulo").val(($(this).val()).toUpperCase());});
// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////

//Tabelas////////////////////////////////////////////////////////////////////
var tabela_novoPaciente = $("#id_table_novoTitulo").DataTable({
    dom:
        "<'row be-datatable-header'<'col-sm-6 col-md-6 col-lg-6 col-xl-6' <'button_novoTitulo'>><'col-sm-6'f>>" +
        "<'row be-datatable-body'<'col-sm-12'tr>>" +
        "<'row be-datatable-footer'<'col-sm-5'i><'col-sm-7'p>>",

    "bSearch": true,
    "bLengthChange": false,
    "pageLength": 10,
    "paging":   true,
    "responsive": true,
    "ordering": true,
    "info":     true,

    "language": {
        "sEmptyTable": "Nenhum registro encontrado",
        "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
        "sInfoFiltered": "(Filtrados de _MAX_ registros)",
        "sInfoPostFix": "",
        "sInfoThousands": ".",
        "sLengthMenu": "_MENU_ resultados por página",
        "sLoadingRecords": "Carregando...",
        "sProcessing": "Processando...",
        "sZeroRecords": "Nenhum registro encontrado",
        "sSearch": "Pesquisar",
        "oPaginate": {
            "sNext": "Próximo",
            "sPrevious": "Anterior",
            "sFirst": "Primeiro",
            "sLast": "Último"
        },
        "oAria": {
            "sSortAscending": ": Ordenar colunas de forma ascendente",
            "sSortDescending": ": Ordenar colunas de forma descendente"
        }
    },
});

$('.button_novoTitulo').append($('#id_div_button')); // Posiciona o button novoTitulo no cabeçalho da tabela
$('#id_div_button').removeAttr('hidden'); // Exibe o button novoTitulo no cabeçalho da tabela

// Button /////////////////////////////////////////
$('#id_button_modal_novoTitulo').click(function(){
    $('#id_modal_form_titulo form tr').show(); // Mostra todos os outros escondidos
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_titulo').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_titulo h3[id="id_title"]').text('Novo Título'); // Volta para o título original do modal
    $('#id_modal_form_titulo form[id="id_form_editar_titulo"]').prop('id', 'id_form_novo_titulo'); // volta para o id original do formulário
    $('#id_modal_form_titulo button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Salvar Título'); // Volta para o nome original do button do formulário
});

function resetar_campos(){
    $('#id_modal_form_titulo form').trigger("reset"); // reseta todos os campos do formulário
    $("#id_nomeTitulo").removeClass("is-invalid").addClass("is-valid");
    $("#id_nomeTitulo")[0].setCustomValidity('');
}

// validar Título ///////////////////////////////
$("#id_nomeTitulo").keyup(function( event ) {
    $.ajax({
        url: "/configuracoes/buscarTituloAjax",
        data: {'titulo': $(this).val(), 'id_nomeTitulo_original': $('#id_modal_form_titulo form input[id="id_nomeTitulo_original"]').val()},
        dataType: 'json',
        success: function (data) {
             if (data.titulo){
                $("#id_nomeTitulo").removeClass("is-valid").addClass("is-invalid");
                $("#id_nomeTitulo")[0].setCustomValidity("Título já Existe");
            }
            else{
                $("#id_nomeTitulo").removeClass("is-invalid").addClass("is-valid");
                $("#id_nomeTitulo")[0].setCustomValidity('');
            }
        }
    });
});
// validar Título ///////////////////////////////


// Formulários /////////////////////////////////////
$('#id_form_novo_titulo').submit(function(e){
    $("button").prop("disabled",true);
    e.preventDefault();
    $.post("/configuracoes/titulos", $(this).serialize(), function(data){
        if (data.ok){
//            console.log("Novo Título Salvo Com Sucesso!");
            $("button").prop("disabled",false);
            window.location.reload()
        }else{
            if(data.erros['nomeTitulo'] != undefined){
                $("#id_nomeTitulo").addClass("is-invalid");
                $("#id_nomeTitulo")[0].setCustomValidity("Título já Existe");
            }
            $("button").prop("disabled",false);
        }
    }, 'json');
});
// Formulários ////////////////////////////////////


$('#id_table_novoTitulo tbody ').on('click', 'tr button', function () {
    // Modifica os campos do formulário de um novo título para editar título
    $('#id_modal_form_titulo').modal('show'); // Exibe o modal do formulário
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_titulo  h3[id="id_title"]').text('Editar Título'); // Troca o título do modal
    $('#id_modal_form_titulo  form[id="id_form_novo_titulo"]').prop('id', 'id_form_editar_titulo'); // Troca o id do formulário
    $('#id_modal_form_titulo  button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Editar Título'); // Muda o nome do button do formulário

    // Busca as informações do título apartir da tabela passando como parâmetro o valor do button (Id do título)
    $.ajax({
        url: "/configuracoes/buscarDadosTituloAjax",
        data: {'id_titulo': $(this).val()}, // Recebe o id do título pelo value do button
        dataType: 'json',
        success: function (data) {
//            console.log(data)
            $('#id_modal_form_titulo form').trigger("reset");
            $('#id_modal_form_titulo form input[id="id_nomeTitulo"]').val(data.nomeTitulo);
            $('#id_modal_form_titulo form input[id="id_nomeTitulo_original"]').val(data.nomeTitulo);

            $("#id_status").val(data.status).trigger('change');
            $('#id_modal_form_titulo form input[id="id_titulo"]').val(data.id_titulo);
        }
    });
});