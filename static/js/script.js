//$( document ).ready(
$(document).ready(function(){
    start()
})

function start()
{
    console.log("ready")
    $(".picture").delegate(this,'click',function() {
        var picture1 = $(this).attr("src");
        // messy as shit but it condenses two identical functions
        var picture2 = $("#"+(parseInt($(this).attr("class").split(" ").pop())=='pic1' ? 'pic2' : 'pic1')).attr("src");
        // change to object to make less janky later
        var returninfo = "picture1=" + picture1 + "&picture2=" + picture2
        $(this).toggleClass("active")
        setTimeout(function() {
            $("#selection").slideUp(300);
            $("#selection").load("catmash #selection", returninfo, function() {
                $("#selection").fadeIn(400);
                $(this).toggleClass("active");
                start();
            });
        }, 1500);
    })//click
}//function
