
$('#id_form_nova_senha').submit(function(e){
    $("button").prop("disabled",true);
    e.preventDefault();
    $.post("/usuario/conta", $(this).serialize(), function(data){

		if(data.ok){
			$('#id_modal').modal('show')
			setTimeout(function(){location.href="{% url 'logout' %}"}, 3000);
		}else{

			$("#id_old_password").removeClass("is-invalid").addClass("is-valid");
			$("#id_new_password1").removeClass("is-invalid").addClass("is-valid");
			$("#id_new_password2").removeClass("is-invalid").addClass("is-valid");


			if(data.erros["old_password"] != undefined){
				$.gritter.add({
					title: 'Senha Atual',
					text: data.erros.old_password,
					class_name: 'color danger'
				});
				$("#id_old_password").removeClass("is-valid").addClass("is-invalid");

			}
			if(data.erros["new_password1"] != undefined){
				$.gritter.add({
					title: 'Nova Senha',
					text: data.erros.new_password1,
					class_name: 'color danger'
				});
				$("#id_new_password1").removeClass("is-valid").addClass("is-invalid");

			}
			if(data.erros["new_password2"] != undefined){
				$.gritter.add({
					title: 'Confirmar Senha',
					text: data.erros.new_password2,
					class_name: 'color danger'
				});
				$("#id_new_password2").removeClass("is-valid").addClass("is-invalid");

			}
		}

		$("button").prop("disabled",false);
    }, 'json');
});