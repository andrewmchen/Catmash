//$( document ).ready(
$(document).ready(function(){
    start()
}
)
        function start()
        {
            console.log("ready")
            $( "#picture1" ).delegate(this,'click',function()
                {
                    var picture1=$("#picture1 img").attr("src");
                    var picture2=$("#picture2 img").attr("src"); 
                    var returninfo=picture1+"|"+picture2 // change to object to make less janky later
                    $('#selection').load("picture #selection",returninfo,function() {start()} ); //
                }//function
            )//live
        }//function
    //)
