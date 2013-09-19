$(document).ready(function(){
	start(0)
}
)
function start(number){
	$( "#nextpage").delegate(this,'click',function()
		{
			number=number+10
			var returninfo="number="+number	
			$("#list").load("top #list",returninfo,function(){})
		}//function
	)//delegate
	$( "#backpage").delegate(this, 'click', function()
		{
			number=number-10
			var returninfo="number="+number
			$("#list").load("top #list",returninfo,function(){
		if(number<10)
		{
			number=0
		}
			
			
			
			})//load
		}//function
	)//delegate
	
}//start

			

