// Seleciona o item de menu //////////////////
$('#id_list_menu_servico').addClass('active');
$('#id_item_meusServicos').addClass('active');
// Seleciona o item de menu //////////////////

$("#id_nome").keyup(function(event){ $(this).val(this.value.toUpperCase())});

$("#id_preco").maskMoney({ prefix: "R$ ", decimal: ",", thousands: "."});
$("#id_valor1").maskMoney({ prefix: "R$ ", decimal: ",", thousands: "."});
$("#id_valor2").maskMoney({ prefix: "R$ ", decimal: ",", thousands: "."});
$("#id_valor3").maskMoney({ prefix: "R$ ", decimal: ",", thousands: "."});

$("#id_porcentagem1").mask("999 %");
$("#id_porcentagem2").mask("999 %");
$("#id_porcentagem3").mask("999 %");

$("#id_quantSessao").keyup(function( event ) {
    if (this.value.length > 3) this.value = this.value.slice(0,3);
    this.value = this.value.replace(/[^0-9]/g, '');
    if(this.value[0] == '0') this.value = parseInt(this.value)
    if(!this.value) this.value = '0'
});

$("#id_tempo").keyup(function( event ) {
    if (this.value.length > 3) this.value = this.value.slice(0,3);
    this.value = this.value.replace(/[^0-9]/g, '');
    if(this.value[0] == '0') this.value = parseInt(this.value)
    if(!this.value) this.value = '0'
});
$("#id_prazoRetorno").keyup(function( event ) {
    if (this.value.length > 3) this.value = this.value.slice(0,3);
    this.value = this.value.replace(/[^0-9]/g, '');
    if(this.value[0] == '0') this.value = parseInt(this.value)
    if(!this.value) this.value = '0';
});
$("#id_prazoValidade").keyup(function( event ) {
    if (this.value.length > 3) this.value = this.value.slice(0,3);
    this.value = this.value.replace(/[^0-9]/g, '');
    if(this.value[0] == '0') this.value = parseInt(this.value)
    if(!this.value) this.value = '0'
});



$('#summernote').summernote({
	  height: 350,                 // set editor height
	  minHeight: null,             // set minimum height of editor
	  maxHeight: null,             // set maximum height of editor
	  focus: true,                  // set focus to editable area after initializing summernote
	  toolbar: [
		['style', ['bold', 'italic', 'underline', 'clear']],
		['font', ['strikethrough', 'superscript', 'subscript']],
		['fontsize', ['fontsize']],
		['color', ['color']],
		['para', ['ul', 'ol', 'paragraph']],
		['height', ['height']]
  	  ]
});

//Tabelas////////////////////////////////////////////////////////////////////
var tabela_novoServico = $("#id_table_novoServico").DataTable({
    dom:
        "<'row be-datatable-header'<'col-sm-6 col-md-6 col-lg-6 col-xl-6' <'button_novoServico'>><'col-sm-6'f>>" +
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
$('.button_novoServico').append($('#id_div_button')); // Posiciona o button novoServico no cabeçalho da tabela
$('#id_div_button').removeAttr('hidden'); // Exibe o button novoServico no cabeçalho da tabela
//Tabelas/////////////////////////////////////////////////////////////////////

// Button /////////////////////////////////////////
$('#id_button_modal_novoServico').click(function(){
    $('#id_modal_form_servico form tr').show(); // Mostra todos os outros escondidos
    $('#id_modal_form_servico form').trigger("reset"); // reseta todos os campos do formulário
//    RepeaterCardDocumento().limparGrupo();
    $('#id_modal_form_servico').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_servico h3[id="id_title"]').text('Novo Serviço'); // Volta para o título original do modal
    $('#id_modal_form_servico form[id="id_form_editar_servico"]').prop('id', 'id_form_novo_serico'); // volta para o id original do formulário
    $('#id_modal_form_servico button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Salvar Serviço'); // Volta para o nome original do button do formulário
    $("#id_card_documento_2").attr('hidden','true')
    $("#id_card_documento_3").attr('hidden','true')
    $("#id_card_documento_4").attr('hidden','true')
});
$('#id_table_novoServico tbody ').on('click', 'tr button', function () {
    // Modifica os campos do formulário de um novo serviço para editar serviço
    $('#id_modal_form_servico').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_servico  h3[id="id_title"]').text('Editar Serviço'); // Troca o título do modal
    $('#id_modal_form_servico  form[id="id_form_novo_usuario"]').prop('id', 'id_form_editar_servico'); // Troca o id do formulário
    $('#id_modal_form_servico  button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Editar Serviço'); // Muda o nome do button do formulário
    // Busca as informações do serviço apartir da tabela passando como parâmetro o valor do button (Id do serviço)
    $.ajax({
        url: "/servico/buscarDadosServicoAjax",
        data: {'id_servico': $(this).val()}, // Recebe o id do serviço pelo value do button
        dataType: 'json',
        success: function (data) {
            $('#id_modal_form_servico form').trigger("reset");
            $("#id_selectAtivarServico").val(data.ativo).trigger('change');
            $('#id_modal_form_servico form input[id="id_nome"]').val(data.nome);
            $('#id_modal_form_servico form input[id="id_quantSessao"]').val(data.quantSessao);
            $('#id_modal_form_servico form input[id="id_tempo"]').val(data.tempo);
            $('#id_modal_form_servico form input[id="id_preco"]').val(data.preco);
            $('#id_modal_form_servico form input[id="id_prazoRetorno"]').val(data.prazoRetorno);
            $('#id_modal_form_servico form input[id="id_prazoValidade"]').val(data.prazoValidade);
            $('#id_modal_form_servico form input[id="id_servico"]').val(data.id_servico);

            $('#id_modal_form_servico form input[id="id_rateio_1"]').val(data.rateio_1);
            $('#id_modal_form_servico form input[id="id_rateio_2"]').val(data.rateio_2);
            $('#id_modal_form_servico form input[id="id_rateio_3"]').val(data.rateio_3);
            $('#id_modal_form_servico form input[id="id_rateio_4"]').val(data.rateio_4);
            $('#id_modal_form_servico form input[id="id_rateio_5"]').val(data.rateio_5);
            $('#id_modal_form_servico form input[id="id_rateio_6"]').val(data.rateio_6);

            $('#id_modal_form_servico form input[id="id_tipoRateio_1"]').val(data.tipoRateio_1);
            $('#id_modal_form_servico form input[id="id_tipoRateio_2"]').val(data.tipoRateio_2);
            $('#id_modal_form_servico form input[id="id_tipoRateio_3"]').val(data.tipoRateio_3);
            $('#id_modal_form_servico form input[id="id_tipoRateio_4"]').val(data.tipoRateio_4);
            $('#id_modal_form_servico form input[id="id_tipoRateio_5"]').val(data.tipoRateio_5);
            $('#id_modal_form_servico form input[id="id_tipoRateio_6"]').val(data.tipoRateio_6);

            $('#id_modal_form_servico form select[id="id_titulo_1"]').val(data.titulo_1);
            $('#id_modal_form_servico form select[id="id_titulo_2"]').val(data.titulo_2);
            $('#id_modal_form_servico form select[id="id_titulo_3"]').val(data.titulo_3);
            $('#id_modal_form_servico form select[id="id_titulo_4"]').val(data.titulo_4);
            $('#id_modal_form_servico form select[id="id_titulo_5"]').val(data.titulo_5);
            $('#id_modal_form_servico form select[id="id_titulo_6"]').val(data.titulo_6);

            $('#id_modal_form_servico form input[id="id_nomeDocumento_1"]').val(data.nomeDocumento_1);
            $('#id_modal_form_servico form input[id="id_nomeDocumento_2"]').val(data.nomeDocumento_2);
            $('#id_modal_form_servico form input[id="id_nomeDocumento_3"]').val(data.nomeDocumento_3);
            $('#id_modal_form_servico form input[id="id_nomeDocumento_4"]').val(data.nomeDocumento_4);
            $('#id_modal_form_servico form input[id="id_nomeDocumento_5"]').val(data.nomeDocumento_5);
            $('#id_modal_form_servico form input[id="id_nomeDocumento_6"]').val(data.nomeDocumento_6);

            $('#id_modal_form_servico form input[id="id_codeDocumento_1"]').val(data.codeDocumento_1);
            $('#id_modal_form_servico form input[id="id_codeDocumento_2"]').val(data.codeDocumento_2);
            $('#id_modal_form_servico form input[id="id_codeDocumento_3"]').val(data.codeDocumento_3);
            $('#id_modal_form_servico form input[id="id_codeDocumento_4"]').val(data.codeDocumento_4);
            $('#id_modal_form_servico form input[id="id_codeDocumento_5"]').val(data.codeDocumento_5);
            $('#id_modal_form_servico form input[id="id_codeDocumento_6"]').val(data.codeDocumento_6);


            $("#id_card_documento_2").attr('hidden','true')
            $("#id_card_documento_3").attr('hidden','true')
            $("#id_card_documento_4").attr('hidden','true')
            $("#id_card_documento_5").attr('hidden','true')
            $("#id_card_documento_6").attr('hidden','true')


            for(i = 1; i <=6; i++){
                if($("#id_codeDocumento_"+i).val() != "" || $("#id_nomeDocumento_"+i).val() != ""){
                    $("#id_card_documento_"+i).removeAttr('hidden');
                }
                if($("#id_rateio_"+i).val() != ""){
                    $("#id_card_regra_"+i).removeAttr('hidden');
                    var tipoRateio = $("#id_tipoRateio_"+i).val()
                    if(tipoRateio == "%"){
                        $($($($($("#id_card_regra_"+i).children().children()[1]).children().children()[0]).children().children()[2]).children()[0]).text('%')
                        $($($($("#id_card_regra_"+i).children().children()[1]).children().children()[0]).children().children()[0]).attr('placeholder','Rateio em Porcentagemm ')
                    }
                }
            }

        }
    });
});
// Button ////////////////////////////////////////


/ Formulários /////////////////////////////////////
$('#id_form_novo_servico').submit(function(e){
    $("#id_button_modal").prop("disabled",true);
    e.preventDefault();
    $.post("/servico/meusServicos", $(this).serialize(), function(data){
        if (data.ok){
            console.log("Novo Serviço Salvo Com Sucesso!!!!!!");
            window.location.reload()
        }else{
            console.log(data.msg);
            $("button").prop("disabled",false);
        }
    }, 'json');
});
// Formulários ////////////////////////////////////


// Regras //////////////////////////////////////////
$("#id_rateio_1").maskMoney({ decimal: ",", thousands: "."})
$("#id_rateio_2").maskMoney({ decimal: ",", thousands: "."})
$("#id_rateio_3").maskMoney({ decimal: ",", thousands: "."})
$("#id_rateio_4").maskMoney({ decimal: ",", thousands: "."})
$("#id_rateio_5").maskMoney({ decimal: ",", thousands: "."})
$("#id_rateio_6").maskMoney({ decimal: ",", thousands: "."})
var RepeaterCardRegra = function(){
    return{
        desativarCard: function(id){
             $("#id_card_regra_"+id).attr('hidden','true');
             $("#id_rateio_"+id).val("");
        },
        maisUm: function(){
            for(i = 2; i <= 6; i++){
                if($("#id_card_regra_"+i).attr('hidden')){
                    $("#id_card_regra_"+i).removeAttr('hidden');
                    break;
                }
            }
        },
        rateio: function(id, texto){
            $($($(id).parents()[1]).children()[0]).text(texto)
            var grupo = $($(id).parents()[2]).children()
            var rateio = grupo[0]
            var tipoRateio = grupo[1]
            if(texto == "R$"){
                $(rateio).attr('placeholder', 'Rateio em Reais')
                $(rateio).maskMoney({ decimal: ",", thousands: "."})
            }
            else if(texto == "%") $(rateio).attr('placeholder', 'Rateio em Porcentagem')


            $(tipoRateio).val(texto)
        },
    }
}
// Regras /////////////////////////////////////////////////

// Documentos ////////////////////////////////////////////
var RepeaterCardDocumento = function(){
    return{
        desativarCard: function(id){
             $("#id_card_documento_"+id).attr('hidden','true');
             $("#id_nomeDocumento_"+id).val("");
             $("#id_codeDocumento_"+id).val("");
        },
        maisUm: function(){
            for(i = 2; i <= 6; i++){
                if($("#id_card_documento_"+i).attr('hidden')){
                    $("#id_card_documento_"+i).removeAttr('hidden');
                    $("#id_nomeDocumento_"+i).val("");
                    $("#id_codeDocumento_"+i).val("");
                    break;
                }
            }
        }
    }
}
// Documentos ////////////////////////////////////////////


$('#id_button_documento_1').click(function(){
  var id = ($(this).attr('data-id'));
  $('#summernote').summernote('reset');
  $("#id_button_salvar").attr("data-id", id);
  $('#summernote').summernote('code', '');
  $('#summernote').summernote('code', $('#id_codeDocumento_'+id).val());
});
$('#id_button_documento_2').click(function(){
  var id = ($(this).attr('data-id'));
  $('#summernote').summernote('reset');
  $("#id_button_salvar").attr("data-id", id);
  $('#summernote').summernote('code', '');
  $('#summernote').summernote('code', $('#id_codeDocumento_'+id).val());});
$('#id_button_documento_3').click(function(){
  var id = ($(this).attr('data-id'));
  $('#summernote').summernote('reset');
  $("#id_button_salvar").attr("data-id", id);
  $('#summernote').summernote('code', '');
  $('#summernote').summernote('code', $('#id_codeDocumento_'+id).val());});
$('#id_button_documento_4').click(function(){
  var id = ($(this).attr('data-id'));
  $('#summernote').summernote('reset');
  $("#id_button_salvar").attr("data-id", id);
  $('#summernote').summernote('code', '');
  $('#summernote').summernote('code', $('#id_codeDocumento_'+id).val());});
$('#id_button_documento_5').click(function(){
  var id = ($(this).attr('data-id'));
  $('#summernote').summernote('reset');
  $("#id_button_salvar").attr("data-id", id);
  $('#summernote').summernote('code', '');
  $('#summernote').summernote('code', $('#id_codeDocumento_'+id).val());});
$('#id_button_documento_6').click(function(){
  var id = ($(this).attr('data-id'));
  $('#summernote').summernote('reset');
  $("#id_button_salvar").attr("data-id", id);
  $('#summernote').summernote('code', '');
  $('#summernote').summernote('code', $('#id_codeDocumento_'+id).val());});

$('#id_nomeDocumento_1').keyup(function(event){ $(this).val(this.value.toUpperCase())});
$('#id_nomeDocumento_2').keyup(function(event){ $(this).val(this.value.toUpperCase())});
$('#id_nomeDocumento_3').keyup(function(event){ $(this).val(this.value.toUpperCase())});
$('#id_nomeDocumento_4').keyup(function(event){ $(this).val(this.value.toUpperCase())});
$('#id_nomeDocumento_5').keyup(function(event){ $(this).val(this.value.toUpperCase())});
$('#id_nomeDocumento_6').keyup(function(event){ $(this).val(this.value.toUpperCase())});


$('#id_button_salvar').click(function(){
   var dataId = ($(this).attr('data-id'));
   $('#id_codeDocumento_'+dataId).val($('#summernote').summernote('code'));
   $('#id_modal_documento').modal('hide')
   $('#summernote').summernote('reset');
});

$('#id_modal_documento').on('shown.bs.modal', function () {
    $("#id_modal_form_servico").attr('hidden', 'true');
})

$('#id_modal_documento').on('hidden.bs.modal', function () {
    $('#id_modal_form_servico').css({'padding':'0 !important', 'overflow-x':'hidden', 'overflow-y':'auto'});
    $("#id_modal_form_servico").removeAttr('hidden');
})