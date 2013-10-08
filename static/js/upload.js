$(document).ready(function(){
function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview').attr('src', e.target.result);
                        $('#preview').Jcrop({
                                trackDocument: true
                        });
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#id_file").change(function(){
    readURL(this);
});


    
});
