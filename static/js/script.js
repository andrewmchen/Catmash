//$( document ).ready(
$(document).ready(function() {
    start();
})

function start() {
    $(".picture").on('click', function() {
        $(".picture").off('click');
        var picture1 = $(this).attr("src");
        var loser = ($(this).attr("id")=='pic1' ? "2" : "1")
        // messy as shit but it condenses two identical functions (nathan)
        var picture2 = $("#pic"+loser).attr("src");
        // change to object to make less janky later
        var returninfo = "picture1=" + picture1 + "&picture2=" + picture2;
        //message to return in http get
        $(this).toggleClass("active");
        $("#selectiontemp").load("catmash", returninfo, function()
            {
                update(loser);
            });
    })//click
}//function

function update(loser) {
    var winner = (loser == "1" ? "2" : "1");
    console.log($("#data").text())
    var data = $("#data").text().split(",");
    var delta = parseFloat(data.pop());
    var lose = parseFloat(data.pop());
    var win = parseFloat(data.pop());

    var win_rate = $("#rate" + winner);
    var lose_rate = $("#rate" + loser);
    var win_pic = $("#pic" + winner);
    var lose_pic = $("#pic" + loser);

    win_rate.addClass("green");
    win_rate.text(win);
    lose_rate.addClass("red");
    lose_rate.text(lose);

    setTimeout(function() {
        jQuery({someValue: (win)}).animate({someValue: (win)+(delta)}, {
        duration: 250,
        easing:'swing', // can be anything
        step: function() { // called on every step
            // Update the element's text with rounded-up value:
            win_rate.text(this.someValue.toFixed(5));
            }
        });

        jQuery({someValue: (lose)}).animate({someValue: (lose)-(delta)}, {
        duration: 250,
        easing:'swing', // can be anything
        step: function() { // called on every step
            // Update the element's text with rounded-up value:
            lose_rate.text(this.someValue.toFixed(5));
            }
        });
    }, 500);


    $("#rating").attr("class","info"); // remove hidden on rating

    setTimeout(function() {
        $("#selection").slideUp(200);
        setTimeout(function() {
            $("#pic1").replaceWith($("#p1")); // picture in selectiontemp
            $("#pic2").replaceWith($("#p2")); // picture in selectiontemp
            $("#p1").attr("id", "pic1");
            $("#p2").attr("id", "pic2");
            $("#selectiontemp").empty();
        }, 300);
        $("#selection").fadeIn(300);
        $("#pic"+winner).toggleClass("active");
        $("#rating").toggleClass("hidden"); // add hidden on rating
        win_rate.removeClass("green");
        lose_rate.removeClass("red");
        start();
    }, 1200);

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
