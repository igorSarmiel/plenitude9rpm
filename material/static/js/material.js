$(document).ready(function(){

$(".btn_delete").on('click', function(event){
        var id = $(this).data('id');
        var modal = $("#confirm-delete");
        modal.find(".modal-body").text("Deletar este registro ? Essa ação é irreversivel.")
        modal.find("#btn_ok").attr("href","/material/deletar/"+id);
        modal.modal('show');
    });

});