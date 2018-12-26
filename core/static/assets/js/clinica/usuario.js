
// Mascaras //////////////////////////////////
$("#id_telefone").mask("+ 55 (99) 9999-9999");
$("#id_celular").mask("+ 55 (99) 99999-9999");
/////////////////////////////////////////////

//Tabelas///////////////////////////////////
$("#id_table_novoUsuario").dataTable({
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

var tabela =  $("#id_table_modal_novoUsuario").DataTable({
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


$("#id_nomeCompleto").keyup(function( event ) {
    $("#id_nomeCompleto").val(($(this).val()).toUpperCase());
});

$("#id_enderecoCompleto").keyup(function( event ) {
    $("#id_enderecoCompleto").val(($(this).val()).toUpperCase());
});

$("#id_email").keyup(function( event ) {

    $("#id_email").val(($(this).val()).toLowerCase());
    $.ajax({
    url: "/usuario/buscarEmailAjax",
    data: {'email': $(this).val()},
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


//Formulários

$('#id_form_novo_usuario').submit(function(e){
    $("#id_funcionalidadeUsuario").val(getSelectTableNovoUsuario());
    $("button").prop("disabled",true);
    e.preventDefault();
    $.post("/usuario/novoUsuario", $(this).serialize(), function(data){
        if (data.ok){
            console.log("Novo Usuário Salvo Com Sucesso!");
            //$('#id_form_novo_usuario').trigger("reset"); // Reseta o formulário
            $("button").prop("disabled",false);
            window.location.reload()
        }else{
            console.log("Erro ao Salvar um Novo Usuário");
            $("button").prop("disabled",false);
            alert(data.erros.email);
        }
    }, 'json');
});



function getSelectTableNovoUsuario(){

    var funcionalidades = '{"linhas":[';
    for(linha = 0; linha < tabela.data().length; linha++){
        var object_field = tabela.row(linha).nodes().to$(); // Linha da tabela
        var select_list = object_field.find('select'); // Retorna uma lista com a busca de todos os 'Select' da tabela
        var id_user = JSON.parse($(select_list[0]).attr('json')).id_user;
        funcionalidades += '{"id_user":'+id_user+'';
        for(i = 0; i < select_list.length; i++) funcionalidades += ',"' + JSON.parse($(select_list[i]).attr('json')).field + '":"'+$(select_list[i]).val()+'"';
        if(linha != tabela.data().length - 1) funcionalidades += '},';
        else funcionalidades += '}';
    }
    return JSON.stringify(JSON.parse(funcionalidades + ']}'));
}








//console.log($('#id_form_novo_usuario').serializeArray());
//'{ "id_user":"'+id_user+'"}'
//list_names.push(JSON.parse($(select_list[i]).attr('name')).field);

//function getSelectTableNovoUsuario(){
//
//    var funcionalidades_json = JSON.parse('{"linhas":[]}');
//
//    for(linha = 0; linha < tabela.data().length; linha++){
//        var object_field = tabela.row(linha).nodes().to$(); // Linha da tabela
//
//        var select_list = object_field.find('select'); // Retorna uma lista com a busca de todos os 'Select' da tabela
//
//        var select_acesso_agenda_value = $(select_list[0]).val(); // coluna da tabela filtrada por 'select'
//        var select_acesso_financeiro_value = $(select_list[1]).val(); // coluna da tabela filtrada por 'select'
//        var select_acesso_prontuario_value = $(select_list[2]).val(); // coluna da tabela filtrada por 'select'
//
//        var pk_user_line = object_field.find('select').attr('name'); // retorna o json do name do primeiro select
//        var select_json = JSON.parse(pk_user_line);
//        var line_json = JSON.parse('{ "id_user":' + select_json.id_user + ', "fields": {"agenda":"'+ select_acesso_agenda_value +'", "financeiro":"'+ select_acesso_financeiro_value +'", "prontuario":"'+select_acesso_prontuario_value+'"} }');
//        funcionalidades_json.linhas.push(line_json);
//    }
//        //$("#id_funcionalidadeUsuario").val(JSON.stringify(funcionalidades_json));
//        return JSON.stringify(funcionalidades_json);
//}

//name='{"id_user":{{usuario.pk}}, "field":"acesso_agenda"}'
//name='{"id_user":{{usuario.pk}}, "field":"acesso_financeiro"}'