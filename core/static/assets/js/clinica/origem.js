
// Seleciona o item de menu //////////////////
$('#id_list_menu_configuracao').addClass('active');
$('#id_item_origem').addClass('active');
// Seleciona o item de menu //////////////////

// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////
$("#id_nome").keyup(function(event){$("#id_nome").val(($(this).val()).toUpperCase());});
// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////

//Tabelas////////////////////////////////////////////////////////////////////
var tabela_novoOrigem = $("#id_table_novoOrigem").DataTable({
    dom:
        "<'row be-datatable-header'<'col-sm-6 col-md-6 col-lg-6 col-xl-6' <'button_novoOrigem'>><'col-sm-6'f>>" +
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

$('.button_novoOrigem').append($('#id_div_button')); // Posiciona o button novoOrigem no cabeçalho da tabela
$('#id_div_button').removeAttr('hidden'); // Exibe o button novoOrigem no cabeçalho da tabela

// Button /////////////////////////////////////////
$('#id_button_modal_novoOrigem').click(function(){
    $('#id_modal_form_origem form tr').show(); // Mostra todos os outros escondidos
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_origem').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_origem h3[id="id_title"]').text('Nova Origem'); // Volta para o título original do modal
    $('#id_modal_form_origem form[id="id_form_editar_origem"]').prop('id', 'id_form_novo_origem'); // volta para o id original do formulário
    $('#id_modal_form_origem button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Salvar Origem'); // Volta para o nome original do button do formulário
});

function resetar_campos(){
    $('#id_modal_form_origem form').trigger("reset"); // reseta todos os campos do formulário
    $("#id_nome").removeClass("is-invalid").addClass("is-valid");
    $("#id_nome")[0].setCustomValidity('');
}

// validar Origem ///////////////////////////////
$("#id_nome").keyup(function( event ) {
    $.ajax({
        url: "/configuracoes/buscarOrigemAjax",
        data: {'nome': $(this).val(), 'id_nome_original': $('#id_modal_form_origem form input[id="id_nome_original"]').val()},
        dataType: 'json',
        success: function (data) {
            if (data.origem){
                $("#id_nome").removeClass("is-valid").addClass("is-invalid");
                $("#id_nome")[0].setCustomValidity("Origem já Existe");
            }
            else{
                $("#id_nome").removeClass("is-invalid").addClass("is-valid");
                $("#id_nome")[0].setCustomValidity('');
            }
        }
    });
});
// validar Origem ///////////////////////////////


// Formulários /////////////////////////////////////
$('#id_form_novo_origem').submit(function(e){
    $("button").prop("disabled",true);
    e.preventDefault();
    $.post("/configuracoes/origens", $(this).serialize(), function(data){
        if (data.ok){
//            console.log("Novo Origem Salvo Com Sucesso!");
            $("button").prop("disabled",false);
            window.location.reload()
        }else{
            if(data.erros['nome'] != undefined){
                $("#id_nome").addClass("is-invalid");
                $("#id_nome")[0].setCustomValidity("Origem já Existe");
            }
            $("button").prop("disabled",false);
        }
    }, 'json');
});
// Formulários ////////////////////////////////////


$('#id_table_novoOrigem tbody ').on('click', 'tr button', function () {
    // Modifica os campos do formulário de um novo título para editar título
    $('#id_modal_form_origem').modal('show'); // Exibe o modal do formulário
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_origem  h3[id="id_title"]').text('Editar Origem'); // Troca o título do modal
    $('#id_modal_form_origem  form[id="id_form_novo_origem"]').prop('id', 'id_form_editar_origem'); // Troca o id do formulário
    $('#id_modal_form_origem  button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Editar Origem'); // Muda o nome do button do formulário

    // Busca as informações da Origem apartir da tabela passando como parâmetro o valor do button (Id do título)
    $.ajax({
        url: "/configuracoes/buscarDadosOrigemAjax",
        data: {'id_origem': $(this).val()}, // Recebe o id da Origem pelo value do button
        dataType: 'json',
        success: function (data) {
//            console.log(data)
            $('#id_modal_form_origem form').trigger("reset");
            $('#id_modal_form_origem form input[id="id_nome"]').val(data.nome);
            $('#id_modal_form_origem form input[id="id_nome_original"]').val(data.nome);

            $("#id_status").val(data.status).trigger('change');
            $('#id_modal_form_origem form input[id="id_origem"]').val(data.id_origem);
        }
    });
});