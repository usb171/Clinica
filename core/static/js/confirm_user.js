"use strict";

$(document).ready(function () {
    $("#formEnableUser").validate({
        rules: {
            password: {
                required: true,
                minlength: 5
            },
            confirm_password: {
                required: true,
                minlength: 5,
                equalTo: "#password"
            }
        },
        messages: {
            confirm_password: {
                equalTo: 'A confirmação de senha está diferente'
            }
        }
    });
});