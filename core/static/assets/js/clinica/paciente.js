// Seleciona o item de menu //////////////////
$('#id_list_menu_paciente').addClass('active');
$('#id_item_meusPacientes').addClass('active');
// Seleciona o item de menu //////////////////

// Mascaras //////////////////////////////////
$("#id_telefone").mask("+ 55 (99) 9999-9999");
$("#id_celular").mask("+ 55 (99) 99999-9999");



$("#id_cep").mask("99999-999").keyup(function(event){
    var cep = $(this).val().replace(/\D/g,'');
    if (cep.length == 8) {$.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
    if (!("erro" in dados)) {$("#id_rua").val(dados.logradouro);$("#id_bairro").val(dados.bairro);
    $("#id_cidade").val(dados.localidade);$("#id_estado").val(dados.uf);
    $("#id_cep").removeClass("is-invalid").addClass("is-valid");}else{
    $("#id_cep").removeClass("is-valid").addClass("is-invalid");}});}else{
    $("#id_cep").removeClass("is-valid").addClass("is-invalid");}});
$("#id_cpf").mask("000.000.000-00").keyup(function(event){
  var strCPF = $(this).val().replace(/\D+/g,'');/*console.log(strCPF)*/;var Soma;var Resto;Soma = 0;if (strCPF == "00000000000"){
  $("#id_cpf").removeClass("is-valid").addClass("is-invalid");return;}
  for (i=1; i<=9; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);Resto = (Soma * 10) % 11;
  if ((Resto == 10) || (Resto == 11))  Resto = 0;if (Resto != parseInt(strCPF.substring(9, 10)) ){
  $("#id_cpf").removeClass("is-valid").addClass("is-invalid");return;} Soma = 0;
  for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i);Resto = (Soma * 10) % 11;
  if ((Resto == 10) || (Resto == 11))  Resto = 0;if (Resto != parseInt(strCPF.substring(10, 11) ) ){
  $("#id_cpf").removeClass("is-valid").addClass("is-invalid");return;}
  else{$("#id_cpf").removeClass("is-invalid").addClass("is-valid");}
});


$("#id_dataNascimento").mask("00/00/0000", {onKeyPress: function(data, e, field, options){
var dia = data.split('/')[0],mes = data.split('/')[1];if(data.length >=2) if(dia > 31) $('#id_dataNascimento').val('31/');
else if(data.length >=5) if(mes > 12) $('#id_dataNascimento').val(dia+'/12/');}});
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////
$("#id_nomeCompleto").keyup(function(event){$("#id_nomeCompleto").val(($(this).val()).toUpperCase());});
$("#id_enderecoCompleto").keyup(function(event){$("#id_enderecoCompleto").val(($(this).val()).toUpperCase());});
// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////




//Tabelas////////////////////////////////////////////////////////////////////
var tabela_convenio = $("#id_table_convenio").DataTable({
 dom:
        "<'row be-datatable-header'<'col-sm-6 col-md-6 col-lg-6 col-xl-6' <'button_novoPaciente'>><'col-sm-6'f>>" +
        "<'row be-datatable-body'<'col-sm-12'tr>>" +
        "<'row be-datatable-footer'<'col-sm-5'i><'col-sm-7'p>>",
    //dom:"<'row be-datatable-body'<'col-sm-12'tr>>",
    "bSearch": false,
    "bLengthChange": false,
    "pageLength": 5,
    "paging":   false,
    "responsive": false,
    "ordering": false,
    "info":     false,

});
var tabela_novoPaciente = $("#id_table_novoPaciente").DataTable({
    dom:
        "<'row be-datatable-header'<'col-sm-6 col-md-6 col-lg-6 col-xl-6' <'button_novoPaciente'>><'col-sm-6'f>>" +
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
$('.button_novoPaciente').append($('#id_div_button')); // Posiciona o button novoPaciente no cabeçalho da tabela
$('#id_div_button').removeAttr('hidden'); // Exibe o button novoPaciente no cabeçalho da tabela
//Tabelas////////////////////////////////////////////////////////////////////

// Button /////////////////////////////////////////
$('#id_button_modal_novoPaciente').click(function(){
    $('#id_modal_form_paciente form tr').show(); // Mostra todos os outros escondidos
    $('#id_modal_form_paciente form').trigger("reset"); // reseta todos os campos do formulário
    $('#id_modal_form_paciente').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_paciente h3[id="id_title"]').text('Novo Paciente'); // Volta para o título original do modal
    //$('#id_modal_form_paciente form[id="id_form_editar_usuario"]').prop('id', 'id_form_novo_usuario'); // volta para o id original do formulário
    //$('#id_modal_form_paciente button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Salvar Usuário'); // Volta para o nome original do button do formulário
});


$(".select2").select2({ width: '100%'}); // Init Select2
$(".tags").select2({tags: true, width: '100%'}); //Select2 tags









$("#id_link_mais_um_convenio").click(function(envent){
    $("#id_div_grupo_convenio").append(
    '<div class="col-sm-4 col-lg-4 mb-3 mb-sm-0" id='+"id_select_convenio_"+'>' +
       '<label for="id_convenio">Convênio</label>' +
       '<select id="id_convenio" name="convenio" class="form-control select2 select2-lg">' +
           '<option value="PLANO A selected">PLANO A</option>' +
           '<option value="PLANO B">PLANO B</option>' +
           '<option value="PLANO C">PLANO C</option>' +
           '<option value="PLANO D">PLANO D</option>' +
       '</select>' +
    '</div>' +
   '<div class="col-sm-4 col-lg-4 mb-3 mb-sm-0">'+
        '<label for="id_numeroCarteira">Número da Carteira</label>' +
        '<input class="form-control" type="text" id="id_numeroCarteira" name="numeroCarteira" placeholder="00000000" required>' +
    '</div>' +
    '<div class="col-sm-4 col-lg-4 mb-3 mb-sm-0">' +
        '<label for="id_validacaoConvenio">Validação do Convênio</label>' +
        '<input class="form-control" type="text" id="id_validacaoConvenio" name="validacaoConvenio" placeholder="00/00/00" required>' +
    '</div>'+
    '<script>$(".select2").select2({ width: "100%"});$(".tags").select2({tags: true, width: "100%"});</script>'
    );
});