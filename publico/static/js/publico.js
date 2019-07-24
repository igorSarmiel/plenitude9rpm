$(document).ready(function(){

    $('#id_data_nascimento').mask('00/00/0000');
    $('#id_matricula').mask('000.000-0');
    $('.telefone').mask('(00)-0-0000-0000');

    $("#btn_delete").on('click', function(event){
        var id = $(this).data('id');
        var modal = $("#confirm-delete");
        modal.find(".modal-body").text("Deletar este registro ? Essa ação é irreversivel e seus dependentes serão apagados também.")
        modal.find("#btn_ok").attr("href","/publico/deletar/"+id);
        modal.modal('show');
    });

    $(".del_dependente").on('click', function(event){
        var id = $(this).data('id');
        var resp = $(this).data('resp');
        var modal = $("#confirm-delete");
        modal.find(".modal-body").text("Deletar este dependente ? Essa ação é irreversivel.");
        modal.find("#btn_ok").attr("href","/publico/deletar_dependente/"+id+"/"+resp);
        modal.modal('show');

    });

    $("#btn_liberar_material").on('click', function(event){
        var id_mat = $(this).data('id');
        var id_resp = $(this).data('resp');
        var modal = $("#confirm-liberacao");
        modal.find("#btn_ok_conf_liber").attr("href","/material/liberar_material/"+id_mat+"/"+id_resp);
        modal.modal('show');

    });

});