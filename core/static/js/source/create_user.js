let SPMaskBehavior = function (val) {
  return val.replace(/\D/g, '').length === 11 ? '+55 (00) 00000-0000' : '+55 (00) 0000-00009';
},
spOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};

$(document).ready(function(){
  $("#formCreateUser").validate();
  $("#id_cellphone").mask(SPMaskBehavior, spOptions);
  $("#id_fullname").keyup(function( event ) {
    $("#id_fullname").val(($(this).val()).toUpperCase());
  });
  $("#id_email").keyup(function( event ) {
    $("#id_email").val(($(this).val()).toLowerCase());
  });
});
