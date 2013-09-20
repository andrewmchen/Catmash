//$( document ).ready(
$(document).ready(function() {
    start();
})

function start() {
    $(".picture").delegate(this, 'click', function() {
        var picture1 = $(this).attr("src");
        var loser = ($(this).attr("id")=='pic1' ? "2" : "1")
        // messy as shit but it condenses two identical functions
        var picture2 = $("#pic"+loser).attr("src");
        // change to object to make less janky later
        var returninfo = "picture1=" + picture1 + "&picture2=" + picture2;
        $(this).toggleClass("active");
        $("#selectiontemp").load("catmash", returninfo, function() {update(loser);start();});
    })//click
}//function

function update(loser) {
    var winner = (loser == "1" ? "2" : "1");
    console.log($("#data").text())
    var data = $("#data").text().split(",");
    var delta = data.pop();
    var lose = data.pop();
    var win = data.pop();
    console.log(loser);
    console.log(winner);

    var win_rate = $("#rate" + winner);
    var lose_rate = $("#rate" + loser);
    var win_pic = $("#pic" + winner);
    var lose_pic = $("#pic" + loser);

    win_rate.toggleClass("green");
    win_rate.toggleClass("hidden");
    win_rate.text(winner);
    lose_rate.toggleClass("red");
    lose_rate.toggleClass("hidden");
    lose_rate.text(loser);

    setTimeout(function() {
        $("#selection").slideUp(300);
        setTimeout(function() {
            $("#pic1").replaceWith($("#p1"));
            $("#pic2").replaceWith($("#p2"));
            $("#selectiontemp").empty();
        }, 300);
        $("#selection").fadeIn(400);
        $("#pic"+winner).toggleClass("active");
    }, 1500);
}




// //$( document ).ready(
// $(document).ready(function(){
//     start()
// })

// function start()
// {
//     console.log("ready")
//     $(".picture").delegate(this,'click',function() {
//         var picture1 = $(this).attr("src");
//         // messy as shit but it condenses two identical functions
//         var picture2 = $("#"+($(this).attr("id")=='pic1' ? 'pic2' : 'pic1')).attr("src");
//         // change to object to make less janky later
//         var returninfo = "picture1=" + picture1 + "&picture2=" + picture2
//         $(this).toggleClass("active")
//         setTimeout(function() {
//             $("#selection").slideUp(300);
//             $("#selection").load("catmash #selection", returninfo, function() {
//                 $("#selection").fadeIn(400);
//                 $(this).toggleClass("active");
//                 start();
//             });
//         }, 1500);
//     })//click
// }//function
