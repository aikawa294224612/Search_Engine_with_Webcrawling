function onkeydown()
{
	if (window.event.keyCode==13) 
	{
		event.returnValue=false;
	}
}


//for search
function formSubmit()
{
	var search = $('#search').val();
	window.location.href = "/home/"+search;
	$('#search-text').text(search);
}

