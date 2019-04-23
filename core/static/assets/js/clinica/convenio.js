
// Seleciona o item de menu //////////////////
$('#id_list_menu_configuracao').addClass('active');
$('#id_item_convenio').addClass('active');
// Seleciona o item de menu //////////////////

// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////
$("#id_nome").keyup(function(event){$("#id_nome").val(($(this).val()).toUpperCase());});
// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////

//Tabelas////////////////////////////////////////////////////////////////////
var tabela_novoConvenio = $("#id_table_novoConvenio").DataTable({
    dom:
        "<'row be-datatable-header'<'col-sm-6 col-md-6 col-lg-6 col-xl-6' <'button_novoConvenio'>><'col-sm-6'f>>" +
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

$('.button_novoConvenio').append($('#id_div_button')); // Posiciona o button novoConvenio no cabeçalho da tabela
$('#id_div_button').removeAttr('hidden'); // Exibe o button novoConvenio no cabeçalho da tabela

// Button /////////////////////////////////////////
$('#id_button_modal_novoConvenio').click(function(){
    $('#id_modal_form_titulo form tr').show(); // Mostra todos os outros escondidos
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_convenio').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_convenio h3[id="id_title"]').text('Novo Convênio'); // Volta para o Convênio original do modal
    $('#id_modal_form_convenio form[id="id_form_editar_convenio"]').prop('id', 'id_form_novo_convenio'); // volta para o id original do formulário
    $('#id_modal_form_convenio button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Salvar Convênio'); // Volta para o nome original do button do formulário
});

function resetar_campos(){
    $('#id_modal_form_convenio form').trigger("reset"); // reseta todos os campos do formulário
    $("#id_nome").removeClass("is-invalid").addClass("is-valid");
    $("#id_nome")[0].setCustomValidity('');
}

// validar Convênio ///////////////////////////////
$("#id_nome").keyup(function( event ) {
    $.ajax({
        url: "/configuracoes/buscarConvenioAjax",
        data: {'nome': $(this).val(), 'id_nome_original': $('#id_modal_form_convenio form input[id="id_nome_original"]').val()},
        dataType: 'json',
        success: function (data) {
            if (data.convenio){
                $("#id_nome").removeClass("is-valid").addClass("is-invalid");
                $("#id_nome")[0].setCustomValidity("Convênio já Existe");
            }
            else{
                $("#id_nome").removeClass("is-invalid").addClass("is-valid");
                $("#id_nome")[0].setCustomValidity('');
            }
        }
    });
});
// validar Convênio ///////////////////////////////


// Formulários /////////////////////////////////////
$('#id_form_novo_convenio').submit(function(e){
    $("button").prop("disabled",true);
    e.preventDefault();
    $.post("/configuracoes/convenios", $(this).serialize(), function(data){
        if (data.ok){
//            console.log("Novo Convênio Salvo Com Sucesso!");
            $("button").prop("disabled",false);
            window.location.reload()
        }else{
            if(data.erros['nome'] != undefined){
                $("#id_nome").addClass("is-invalid");
                $("#id_nome")[0].setCustomValidity("Convênio já Existe");
            }
            $("button").prop("disabled",false);
        }
    }, 'json');
});
// Formulários ////////////////////////////////////


$('#id_table_novoConvenio tbody ').on('click', 'tr button', function () {
    // Modifica os campos do formulário de um novo convênio para editar convênio
    $('#id_modal_form_convenio').modal('show'); // Exibe o modal do formulário
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_convenio  h3[id="id_title"]').text('Editar Convênio'); // Troca o título do modal
    $('#id_modal_form_convenio  form[id="id_form_novo_convenio"]').prop('id', 'id_form_editar_convenio'); // Troca o id do formulário
    $('#id_modal_form_convenio  button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Editar Convênio'); // Muda o nome do button do formulário

    // Busca as informações do convênio apartir da tabela passando como parâmetro o valor do button (Id do convênio)
    $.ajax({
        url: "/configuracoes/buscarDadosConvenioAjax",
        data: {'id_convenio': $(this).val()}, // Recebe o id do convênio pelo value do button
        dataType: 'json',
        success: function (data) {
            $('#id_modal_form_convenio form').trigger("reset");
            $('#id_modal_form_convenio form input[id="id_nome"]').val(data.nome);
            $('#id_modal_form_convenio form input[id="id_nome_original"]').val(data.nome);

            $("#id_status").val(data.status).trigger('change');
            $('#id_modal_form_convenio form input[id="id_convenio"]').val(data.id_convenio);
        }
    });
});