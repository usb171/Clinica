'use strict';

var SPMaskBehavior = function SPMaskBehavior(val) {
  return 11 === val.replace(/\D/g, '').length ? '+55 (00) 00000-0000' : '+55 (00) 0000-00009';
},
    spOptions = {
  onKeyPress: function onKeyPress(val, e, field, options) {
    field.mask(SPMaskBehavior.apply({}, arguments), options);
  }
};

$(document).ready(function () {
  $("#id_phone").mask(SPMaskBehavior, spOptions);
  $("#id_zip_code").mask("99.999-999");
});