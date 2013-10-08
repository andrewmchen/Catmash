$(document).ready( function() {
	start(0)
});

function start(number) {
	$("#nextpage").delegate(this, 'click', function() {
		number = number + 6;
		var returninfo = "number=" + number;
		$("#list").load("top #list", returninfo);
	});

	$("#backpage").delegate(this, 'click', function() {
		number = number - 6;
		var returninfo = "number=" + number;
		$("#list").load("top #list", returninfo, function() {
			if (number < 6) number = 0;
		});
	});//delegate

};

function zoompic(number) {
	$("#zoom").slideUp(200);
	$("#zoom").html("<img src='"+$("#"+number).attr("src")+"'>");
	$("#zoom").slideDown(200);
}



