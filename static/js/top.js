$(document).ready( function() {
	start(0)
	attachhandler();
	zoompic(0);
});

function start(number) {
	$("#nextpage").delegate(this, 'click', function() {
		number = number + 6;
		var returninfo = "number=" + number;
		$("#list").load("toppic #list", returninfo, function() {
			attachhandler();
		});
	});

	$("#backpage").delegate(this, 'click', function() {
		number = number - 6;
		var returninfo = "number=" + number;
		$("#list").load("toppic #list", returninfo, function() {
			if (number < 6) number = 0;
			attachhandler();
		});
	});//delegate
};

function zoompic(number) {
	$(".thumbnail").toggleClass('active');
	$("#"+number).toggleClass("active");
	$("#zoom").slideUp(500);
	setTimeout(function() {
		$("#zoom").html("<img src='"+$("#"+number).attr("src")+"' height=600px width=600px>");
	}, 500);
	$("#zoom").slideDown(500);
};

function attachhandler() {
	$(".topzoom").on("click", function() {
		zoompic($(this).attr('id'));
	});
};


