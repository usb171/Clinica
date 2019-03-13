// Seleciona o item de menu //////////////////
$('#id_list_menu_paciente').addClass('active');
$('#id_item_meusPacientes').addClass('active');
// Seleciona o item de menu //////////////////

// Mascaras //////////////////////////////////
$("#id_telefone").mask("+ 55 (99) 9999-9999");
$("#id_celular").mask("+ 55 (99) 99999-9999");

// Validar Email /////////////////////////////


$("#id_email").keyup(function( event ) {
    $("#id_email").val(($(this).val()).toLowerCase());
    $.ajax({
        url: "/paciente/buscarEmailAjax",
        data: {'email': $(this).val(), 'email_original': $('#id_modal_form_paciente form input[id="id_email_original"]').val()},
        dataType: 'json',
        success: function (data) {
        console.log("aqui:" + $("#id_dataHora a").text());
            if (data.email){
                $("#id_email").removeClass("is-valid").addClass("is-invalid");
                $("#id_email")[0].setCustomValidity("Email já Existe");
            }
            else{
                $("#id_email").removeClass("is-invalid").addClass("is-valid");
                $("#id_email")[0].setCustomValidity('');
            }
        }
    });
});
// Validar Email /////////////////////////////


$("#id_cep").mask("99999-999").keyup(function(event){
    var cep = $(this).val().replace(/\D/g,'');
    if (cep.length == 8) {$.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados){
    if (!("erro" in dados)) {$("#id_rua").val(dados.logradouro);$("#id_bairro").val(dados.bairro);
    $("#id_cidade").val(dados.localidade);$("#id_estado").val(dados.uf).change();
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



validarData("#id_dataNascimento", "dataNascimento");
validarData("#id_convenioValidade", "convenioValidade");

function validarData(id, campo){
    $(id).mask("99/99/9999", {placeholder: "__/__/____", onKeyPress: function(data, e, field, options){
        var dia = data.split('/')[0], mes = data.split('/')[1], ano = data.split('/')[2]
        console.log(data + " " + id);
        $("#id_idade").val("...");
        if(data.length >= 2)
            if(dia > 31)
                $(id).val('31/');
            else if(dia == 0)
                $(id).val('01/');
        else
            if(data.length >=5)
                if(mes > 12)
                    $(id).val(dia+'/12/');
                else if(mes == 0)
                    $(id).val(dia+'/01/');
                else if(mes == 2 && dia > 28)
                    $(id).val('28/02');

        if(data.length == 10){

            diaSistema = $("#id_dataHora a").text().split('/')[0].split(' ')[0];
            mesSistema = $("#id_dataHora a").text().split('/')[1].split(' ')[0];
            anoSistema = $("#id_dataHora a").text().split('/')[2].split(' ')[0];

            if(ano == 0){ $(id).val(dia+'/'+mes+'/'+anoSistema); ano=anoSistema;}

            if(campo == "dataNascimento"){
                if(ano >= 1930 && ano <= anoSistema){
                    $(id).removeClass("is-invalid").addClass("is-valid");
                    $("#id_idade").removeClass("is-invalid").addClass("is-valid");
                    $(id)[0].setCustomValidity('');
                    if(diaSistema >= dia && mesSistema >= mes)
                        $("#id_idade").val(anoSistema-ano + " anos");
                    else
                        if(ano == anoSistema)
                            $("#id_idade").val("0 anos");
                        else
                            $("#id_idade").val((anoSistema-ano)-1 + " anos");
                }
                else{
                    $(id).removeClass("is-valid").addClass("is-invalid")
                    if(ano < 1930){
                        $(id)[0].setCustomValidity("Data de nascimento muito antiga");
                    }
                    else{
                        $(id)[0].setCustomValidity("Data de nascimento não pode ser maior do que o ano corrente");
                    }
                }
            } else if(campo == "convenioValidade"){

                var dataCampo = new Date(mes+'/'+dia+'/'+ano).setHours(0,0,0,0);
                var dataSistema = new Date(mesSistema+'/'+diaSistema+'/'+anoSistema).setHours(0,0,0,0);

                if (dataCampo < dataSistema) {
                  $(id).removeClass("is-valid").addClass("is-invalid");
                  $(id)[0].setCustomValidity("Convênio expirado");
                }else{
                  $(id).removeClass("is-invalid").addClass("is-valid");
                  $(id)[0].setCustomValidity("");
                }
            }

        } else{
            $(id).removeClass("is-valid").addClass("is-invalid");
//          $("#id_idade").removeClass("is-valid").addClass("is-invalid");
            $(id)[0].setCustomValidity("Data inválida");
        }
    }
    });
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////
$("#id_nomeCompleto").keyup(function(event){$("#id_nomeCompleto").val(($(this).val()).toUpperCase());});
$("#id_enderecoCompleto").keyup(function(event){$("#id_enderecoCompleto").val(($(this).val()).toUpperCase());});
// Maiúsculo ///////////////////////////////////////////////////////////////////////////////////////////////////


$(".select2").select2({ width: '100%'}); // Init Select2
$(".tags").select2({tags: true, width: '100%'}); //Select2 tags


//Tabelas////////////////////////////////////////////////////////////////////
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
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_paciente').modal('show'); // Exibe o modal do formulário
    $('#id_modal_form_paciente h3[id="id_title"]').text('Novo Paciente'); // Volta para o título original do modal
    $('#id_modal_form_paciente form[id="id_form_editar_paciente"]').prop('id', 'id_form_novo_paciente'); // volta para o id original do formulário
    $('#id_modal_form_paciente button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Salvar Paciente'); // Volta para o nome original do button do formulário

});

$('#id_table_novoPaciente tbody ').on('click', 'tr button', function () {
    // Modifica os campos do formulário de um novo paciente para editar paciente
    $('#id_modal_form_paciente').modal('show'); // Exibe o modal do formulário
    resetar_campos(); // Reseta todos os campos do formulário
    $('#id_modal_form_paciente  h3[id="id_title"]').text('Editar Paciente'); // Troca o título do modal
    $('#id_modal_form_paciente  form[id="id_form_novo_paciente"]').prop('id', 'id_form_editar_paciente'); // Troca o id do formulário
    $('#id_modal_form_paciente  button[id="id_button_modal"]').html('<i class="icon mdi mdi-save"></i> Editar Paciente'); // Muda o nome do button do formulário

    // Busca as informações do paciente apartir da tabela passando como parâmetro o valor do button (Id do usuário)
    $.ajax({
        url: "/paciente/buscarDadosPacienteAjax",
        data: {'id_paciente': $(this).val()}, // Recebe o id do paciente pelo value do button
        dataType: 'json',
        success: function (data) {
            $('#id_modal_form_paciente form').trigger("reset");
            $('#id_modal_form_paciente form input[id="id_cpf"]').val(data.cpf);
            $('#id_modal_form_paciente form input[id="id_cep"]').val(data.cep);
            $('#id_modal_form_paciente form input[id="id_rua"]').val(data.rua);
            $('#id_modal_form_paciente form input[id="id_sexo"]').val(data.sexo);
            $('#id_modal_form_paciente form input[id="id_email"]').val(data.email);
            $('#id_modal_form_paciente form input[id="id_email_original"]').val(data.email);
            $('#id_modal_form_paciente form input[id="id_numero"]').val(data.numero);
            $('#id_modal_form_paciente form input[id="id_quadra"]').val(data.quadra);
            $('#id_modal_form_paciente form input[id="id_bairro"]').val(data.bairro);
            $('#id_modal_form_paciente form input[id="id_cidade"]').val(data.cidade);
            $('#id_modal_form_paciente form input[id="id_estado"]').val(data.estado);
            $("#id_estado").val(data.estado).trigger('change');
            $("#id_selectAtivarPaciente").val(data.ativo).trigger('change');
            $('#id_modal_form_paciente form input[id="id_celular"]').val(data.celular);
            $('#id_modal_form_paciente form input[id="id_telefone"]').val(data.telefone);
            $("#id_profissao").val(data.profissao.split(",")).trigger('change');
            $('#id_modal_form_paciente form textarea[id="id_observacao"]').val(data.observacao);
            $('#id_modal_form_paciente form input[id="id_complemento"]').val(data.complemento);
            $("#id_estadoCivil").val(data.estadoCivil).trigger('change');
            $('#id_modal_form_paciente form input[id="id_nomeCompleto"]').val(data.nomeCompleto);
            $('#id_modal_form_paciente form input[id="id_grupoConvenio"]').val(data.grupoConvenio);
            $('#id_modal_form_paciente form input[id="id_dataNascimento"]').val(data.dataNascimento);
            $('#id_modal_form_paciente form input[id="id_idade"]').val(data.idade);

            $("#id_nomeFamiliar").val(data.nomeFamiliar).trigger('change');
            $("#id_grauParentesco").val(data.grauParentesco).trigger('change');

            $('#id_modal_form_paciente form input[id="id_paciente"]').val(data.id_paciente);

            path = data.image_path;
            imageObj.src = path.replace('core','');

            var RegExp = /["|']/g;
            convenioGrupos = JSON.parse(data.grupoConvenio);
            for(k in convenioGrupos){
                if( k != "'0'"){
                    adicionar_linha_convenio(parseInt(k.replace(RegExp, '')), convenioGrupos[k].convenio, convenioGrupos[k].numero, convenioGrupos[k].validade);
                }else{
                    $("#id_convenio").val(convenioGrupos[k].convenio).trigger("change");
                    $('#id_modal_form_paciente form input[id="id_convenioCarteira"]').val(convenioGrupos[k].numero);
                    $('#id_modal_form_paciente form input[id="id_convenioValidade"]').val(convenioGrupos[k].validade);
                }
            }

            //Permissões //////////////////////////////////////
            if($("#id_button_modal").val() == undefined){
                $('form *').prop('disabled', true); // Desativa todos os campos do formulário para edição
                $('#id_button_mais_um_convenio').prop('hidden', true); // Esconde a div que contém o button mais um convênio para edição
                $("div[id*='id_button_menos_um_convenio']").prop('hidden', true); // Esconde os buttons de menos um convênio
                $("div[class='col-sm-3 col-lg-3 mb-3 mb-sm-0']").toggleClass('col-sm-4 col-lg-4 mb-4 mb-sm-0'); // Alinha os campos do convênio após remover os button de ação
            }
            else $('form *').prop('disabled', false); // Reativa todos os campos do formulário para edição
            //Permissões //////////////////////////////////////
        }
    });
});
// Button /////////////////////////////////////////

function resetar_campos(){
    $('#id_modal_form_paciente form').trigger("reset"); // reseta todos os campos do formulário
    $("#id_profissao").val("------").trigger('change'); // reseta o campo profissão
    $("#id_convenio").val("------").trigger('change'); // reseta o campo profissão
    var gruposConvenioSize = $("#id_div_grupo_convenio .form-group.row").length;
    for(var i = 1; i < gruposConvenioSize; i++) // reseta os grupos do convenio
        remove_linha_grupo_convenio("id_button_menos_um_convenio_"+i);

    $("#id_cep").removeClass("is-invalid");
    $("#id_cep").removeClass("is-valid");

    $("#id_cpf").removeClass("is-invalid");
    $("#id_cpf").removeClass("is-valid");
}

// Convenio ///////////////////////////////////////////////////////////////////////////////////////////////

function remove_linha_grupo_convenio(id){
    $("#" + id + "_row").remove();
    atualiza_ids_grupo_convenio("id_div_grupo_convenio", "id_button_menos_um_convenio");
}

function adicionar_linha_convenio(count="", convenio="", numero="", validade=""){
    grupos = $("#id_div_grupo_convenio .row");
    count = grupos.length;

    $("#id_div_grupo_convenio").append(
        '<div class="form-group row pt-0 pb-0"  id="id_button_menos_um_convenio_'+count+'_row"  count='+count+'>' +
            '<div class="col-sm-4 col-lg-4 mb-3 mb-sm-0">' +
                '<label for="id_convenio_'+count+'">Convênio </label>' +
                '<select id="id_convenio_'+count+'" name="convenio" class="form-control select2 select2-lg">' +
                    get_options_select_convenio() +
                '</select>' +
            '</div>' +
            '<div class="col-sm-4 col-lg-4 mb-3 mb-sm-0">' +
                '<label for="id_convenioCarteira_'+count+'">Número Carteira </label>' +
                '<input class="form-control" type="number" id="id_convenioCarteira_'+count+'" name="numeroCarteira" value="'+numero+'">' +
            '</div>' +
            '<div class="col-sm-3 col-lg-3 mb-3 mb-sm-0">' +
                '<label for="id_convenioValidade_'+count+'">Validade </label>' +
                '<input class="form-control" type="text" id="id_convenioValidade_'+count+'" name="convenioValidade" value="'+validade+'">' +
            '</div>' +
            '<div class="col-sm-1 col-lg-1 mb-1 mb-sm-1 icon-container icon-visible text-center"  id="id_button_menos_um_convenio_'+count+'" onclick="remove_linha_grupo_convenio(id);" >' +
                '<div class="icon"><span class="mdi mdi-minus-circle"></span></div>' +
            '</div>' +

        '</div>' +

            '<script>' +
                '$(".select2").select2({ width: "100%"}); $(".tags").select2({tags: true, width: "100%"});'+
                '$("#id_convenio_'+count+'").val("'+convenio+'").trigger("change");' +
                'validarData("#id_convenioValidade_'+count+'", "convenioValidade");' +
            '</script>'
    );
}

function atualiza_ids_grupo_convenio(idGrupo, idButton){
    linhas = $("#" + idGrupo + " .row");
    quant = linhas.length;
    for(l = 1; l < quant; l++){
        $(linhas[l]).attr('count', l);
        $(linhas[l]).attr('id', idButton + "_" + l + "_row");
        $($(linhas[l]).children()[3]).attr("id", "id_button_menos_um_convenio_" + l);

        $($($($(linhas[l]).children()[0])).children()[0]).attr("id", "id_convenio_" + l).attr("for", "id_convenio_" + l);
        $($($($(linhas[l]).children()[0])).children()[1]).attr("id", "id_convenio_" + l);

        $($($($(linhas[l]).children()[1])).children()[0]).attr("id", "id_convenioCarteira_" + l).attr("for", "id_convenioCarteira_" + l);;
        $($($($(linhas[l]).children()[1])).children()[1]).attr("id", "id_convenioCarteira_" + l);

        $($($($(linhas[l]).children()[2])).children()[0]).attr("id", "id_convenioValidade_" + l).attr("for", "id_convenioValidade_" + l);;
        $($($($(linhas[l]).children()[2])).children()[1]).attr("id", "id_convenioValidade_" + l);
    }
}

function get_json_convenio(){ // Retorna em json os dados dos grupos do convênio
    var grupos_size  = $("#id_div_grupo_convenio .form-group.row").length;
    var out = JSON.parse("{}");
    for(var i = 0; i < grupos_size; i++){
        var grupo = $($("#id_div_grupo_convenio .form-group.row")[i]);
        out["'"+grupo.attr('count')+"'"] = JSON.parse('{ "convenio": "'+ grupo.find("select").val() + '", "numero": "' + $(grupo.find("input")[0]).val() + '", "validade": "' + $(grupo.find("input")[1]).val() + '"}');
    }
    return JSON.stringify(out);
}

function get_options_select_convenio(){ // Retorna os options do select convenho
    var out = "";
    var options = $('#id_convenio option');
    for(var i = 0; i < options.length; i++)out += "<option>" + options[i].value + "</option>";
    return out;
}

// Convenio ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




// WebCam ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
const errorMsgElement = document.querySelector('span#errorMsg');
var imageObj = new Image();
var stream = null;
const constraints = {
  audio: false,
  video: {
    width: 2000, height: 2000
  }
};

async function initWebCam() {
  try {
    stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMsgElement.innerHTML = 'navigator.getUserMedia error:${e.toString()}';
  }
}

function desativarWebCam(){
    stream.getTracks()[0].stop();
}

function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;
}

function take(){
	context.drawImage(video, 5, 5, 240 + 50, 140);
}

imageObj.onload = function() {
    context.restore();
    context.drawImage(imageObj, 5, 5, 240 + 50, 140);

};

// WebCam ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



// Formulários /////////////////////////////////////
$('#id_form_novo_paciente').submit(function(e){
    $("#id_grupo_convenio").val(get_json_convenio());
    $("#id_imagem_paciente").val(canvas.toDataURL());
    $("#id_profissao_input").val($("#id_profissao").select2("val"));
    $("button").prop("disabled",true);

    desativarWebCam();

    e.preventDefault();
    $.post("/paciente/meusPacientes", $(this).serialize(), function(data){
        if (data.ok){
            console.log("Novo Paciente Salvo Com Sucesso!");
            $("button").prop("disabled",false);
            window.location.reload()
        }else{
            console.log(data.msg);
            $("button").prop("disabled",false);
        }
    }, 'json');
});
// Formulários ////////////////////////////////////

