$(document).ready(function(){

    $("#id_cpf").mask("999.999.999-99");

    $("form#form-customer").submit(function(){
        var cpf_field = $('#id_cpf');
        if(cpf_field.val()){
            cpf_field.val(cpf_field.val().replace(/[^\d]+/g,''));
        }
    });

});
