// Seleciona o item de menu //////////////////
$('#id_list_menu_usuario').addClass('active');
$('#id_item_meusUsuarios').addClass('active');
// Seleciona o item de menu //////////////////

// Mascaras //////////////////////////////////
$("#id_telefone").mask("+ 55 (99) 9999-9999");
$("#id_celular").mask("+ 55 (99) 99999-9999");
/////////////////////////////////////////////

// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////
$("#id_nomeCompleto").keyup(function(event){$("#id_nomeCompleto").val(($(this).val()).toUpperCase());});
$("#id_enderecoCompleto").keyup(function(event){$("#id_enderecoCompleto").val(($(this).val()).toUpperCase());});
// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////

// Validar Email /////////////////////////////
$("#id_email").keyup(function( event ) {
    $("#id_email").val(($(this).val()).toLowerCase());
    $.ajax({
        url: "/usuario/buscarEmailAjax",
        data: {'email': $(this).val(), 'email_original': $('#id_modal_form_usuario form input[id="id_email_original"]').val()},
        dataType: 'json',
        success: function (data) {
            if (data.email){
                //console.log("Email Inválido!!");
                $("#id_email").removeClass("is-valid").addClass("is-invalid");
                $("#id_email")[0].setCustomValidity("Email já Existe");
            }
            else{
                //console.log("Email OK");
                $("#id_email").removeClass("is-invalid").addClass("is-valid");
                $("#id_email")[0].setCustomValidity('');
            }
        }
    });
});
// Validar Email /////////////////////////////


//Tabelas////////////////////////////////////////////////////////////////////
var tabela_novoUsuario = $("#id_table_novoUsuario").DataTable({
    dom:
        "<'row be-datatable-header'<'col-sm-6 col-md-6 col-lg-6 col-xl-6' <'button_novoUsuario'>><'col-sm-6'f>>" +
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
$('.button_novoUsuario').append($('#id_div_button')); // Posiciona o button novoUsuario no cabeçalho da tabela
$('#id_div_button').removeAttr('hidden'); // Exibe o button novoPaciente no cabeçalho da tabela

var tabela_funcionalidades =  $("#id_table_funcionalidades").DataTable({

        "bSearch": true,
        "bLengthChange": false,
        "pageLength": 5,
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
//Tabelas/////////////////////////////////////////////////////////////////////


// Button /////////////////////////////////////////
$('#id_button_modal_novoUsuario').click(function(){
    $('#id_modal_form_usuario form tr').show(); // Mostra todos os outros escondidos
    $('#id_modal_form_usuario form').trigger("reset"); // reseta todos os campos do formulário
    $('#id_modal_form_usuario').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_usuario h3[id="id_title"]').text('Novo Usuário'); // Volta para o título original do modal
    $('#id_modal_form_usuario form[id="id_form_editar_usuario"]').prop('id', 'id_form_novo_usuario'); // volta para o id original do formulário
    $('#id_modal_form_usuario button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Salvar Usuário'); // Volta para o nome original do button do formulário

});
$('#id_table_novoUsuario tbody ').on('click', 'tr button', function () {
    // Modifica os campos do formulário de um novo usuário para editar usuário
    $('#id_modal_form_usuario').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_usuario  h3[id="id_title"]').text('Editar Usuário'); // Troca o título do modal
    $('#id_modal_form_usuario  form[id="id_form_novo_usuario"]').prop('id', 'id_form_editar_usuario'); // Troca o id do formulário
    $('#id_modal_form_usuario  button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Editar Usuário'); // Muda o nome do button do formulário

    // Busca as informações do usuário apartir da tabela passando como parâmetro o valor do button (Id do usuário)
    $.ajax({
        url: "/usuario/buscarDadosUsuarioAjax",
        data: {'id_user': $(this).val()}, // Recebe o id do usuário pelo value do button
        dataType: 'json',
        success: function (data) {
            $('#id_modal_form_usuario form').trigger("reset");

            $("#id_email").removeClass("is-invalid").addClass("is-valid");

            $('#id_modal_form_usuario form input[id="id_nomeCompleto"]').val(data.nomeCompleto);
            $('#id_modal_form_usuario form input[id="id_email"]').val(data.email);
            $('#id_modal_form_usuario form input[id="id_email_original"]').val(data.email);
            $('#id_modal_form_usuario form input[id="id_telefone"]').val(data.telefone);
            $('#id_modal_form_usuario form input[id="id_celular"]').val(data.celular);
            $('#id_modal_form_usuario form input[id="id_enderecoCompleto"]').val(data.enderecoCompleto);

            $('#id_modal_form_usuario form select[id="id_titulo"]').val(data.titulo);

            $('#id_modal_form_usuario form select[id="id_selectAtivarUsuario"]').val(data.ativo);
            $('#id_modal_form_usuario form select[id="id_selectAtivarAdministrador"]').val(data.admin);
            $('#id_modal_form_usuario form select[id="id_selectAtivarAgendaPropira"]').val(data.agendaPropria);

            $('#id_modal_form_usuario form select[id="id_selectEstoque"]').val(data.controleEstoque);
            $('#id_modal_form_usuario form select[id="id_selectProntuario"]').val(data.controleProntuario);

            $('#id_modal_form_usuario form input[id="id_user"]').val(data.id_user); // ID do usuário a ser editado

            $('#id_modal_form_usuario form tr').show(); // Mostra todos os outros escondidos
            $('#id_modal_form_usuario form tr[id="'+ data.id_user +'"]').hide(); // Esconde somente o usuário selecionado na tabela que será editado

            setSelectTableNovoUsuario(tabela_funcionalidades, data.funcionalidadeUsuario); // Seta as funcionalidades na tabela

            if(data.id_user == data.id_user_logado){
                $('#id_modal_form_usuario form select[id="id_selectAtivarAdministrador"]').css('pointer-events','none');
                $('#id_modal_form_usuario form select[id="id_selectAtivarAdministrador"]').css('border-color','#a9a211');
            }else{
                $('#id_modal_form_usuario form select[id="id_selectAtivarAdministrador"]').css('border-color','#d5d8de');
                $('#id_modal_form_usuario form select[id="id_selectAtivarAdministrador"]').css('pointer-events','visible');
            }

        }
    });
});
// Button ////////////////////////////////////////

/**
 * Busca os atributos json de cada Select;
 * Separa o ID do usuário e seus devidos campos de acesso;
 * Monta posteriormente um json com a configuração da tabela.
 *
 * @param   {Table}   Parametro obrigatório
 * @returns {JSON}
 */
function getSelectTableNovoUsuario(table){
    var funcionalidades = '{"linhas":[';
    for(linha = 0; linha < table.data().length; linha++){
        var object_field = table.row(linha).nodes().to$(); // Linha da tabela
        var select_list = object_field.find('select'); // Retorna uma lista com a busca de todos os 'Select' da tabela
        var id_user = JSON.parse($(select_list[0]).attr('json')).id_user;
        funcionalidades += '{"id_user":'+id_user+'';
        for(i = 0; i < select_list.length; i++) funcionalidades += ',"' + JSON.parse($(select_list[i]).attr('json')).field + '":"'+$(select_list[i]).val()+'"';
        if(linha != table.data().length - 1) funcionalidades += '},';
        else funcionalidades += '}';
    }
    return JSON.stringify(JSON.parse(funcionalidades + ']}'));
}

/**
 * Faz a leitura de um valor JSON;
 * Identifica cada usuário da tabela pelo ID;
 * Seta cada valor nos seus devidos campos select.
 *
 * @param   {Table, JSON}   Parametro obrigatório
 */
function setSelectTableNovoUsuario(table, json){
    var linhas_json = JSON.parse(json).linhas;
    for(l = 0; l < table.data().length; l++){
        var linha_id_user = $(table.row(l).nodes().to$().find("td")).html();
        for(i = 0; i < linhas_json.length; i++){
            if(linhas_json[i].id_user == linha_id_user){
                $(table.row(l).nodes().to$().find("select")[0]).val(linhas_json[i].acesso_agenda);
                $(table.row(l).nodes().to$().find("select")[1]).val(linhas_json[i].acesso_financeiro);
                $(table.row(l).nodes().to$().find("select")[2]).val(linhas_json[i].acesso_prontuario);
            }
        }
    }
}


// Formulários /////////////////////////////////////
$('#id_form_novo_usuario').submit(function(e){
    $("#id_funcionalidadeUsuario").val(getSelectTableNovoUsuario(tabela_funcionalidades));
    $("button").prop("disabled",true);
    e.preventDefault();
    $.post("/usuario/meusUsuarios", $(this).serialize(), function(data){
        if (data.ok){
            console.log("Novo Usuário Salvo Com Sucesso!");
            $("button").prop("disabled",false);
            window.location.reload()
        }else{
            console.log(data.msg);
            $("button").prop("disabled",false);
        }
    }, 'json');
});
// Formulários ////////////////////////////////////

//Permissões //////////////////////////////////////
if($("#id_button_modal").val() == undefined) $('form *').prop('disabled', true); // Desativa todos os campos do formulário para edição
else $('form *').prop('disabled', false); // Reativa todos os campos do formulário para edição
//Permissões //////////////////////////////////////