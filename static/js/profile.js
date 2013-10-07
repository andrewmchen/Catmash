$(document).ready(function(){
        $(".edit").on('click',function(){ 
            $(this).find('div').toggle("fast");
        }) // on


        $("#delete").on('click',function(){
            $(this).off('click')
        });
    
});
