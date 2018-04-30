$(function() {

	// iterate on each of the rows and populate the information from the API.
	$('#myTbody tr').each(function() {
		var tr = $(this);
    	var cityName = $(this).find("td:eq(0)");
    	var temp_td = $(this).find("td:eq(1)");
		var icon_td = $(this).find("td:eq(2)");

		$.ajax({
			// default local address for PyCharm local inviroment
			url : "http://127.0.0.1:5000/weather/"+cityName.html(),
			type: "GET",
			success: function(data)
			{
				// change citi name in case we will allow user input for more locations, the weather API will accept slightly mispelled names and correct.
				cityName.html(data.name);
				temp_td.html(Math.round(data.temp));
				icon_td.html('<img src="'+data.icon+'" />');
				// populate the extra info in a hidden <tr> to avoid extra calls if user want more info.
				$('<tr style="display: none !important;"><table><tr>'+
					'<td>Humidity: '+data.humid+'</td>'+
					'<td>Weather: '+data.main_descr+'</td>'+
					'<td>Max. Temp: '+Math.round(data.max_t)+'</td>'+
					'<td>Min. Temp: '+Math.round(data.min_t)+'</td></tr>'
				).insertAfter(tr).hide();
			},
			error: function (jqXHR, statusText , errorThrown)
			{
				temp_td.html('unavailable');
				icon_td.html('unavailable');
				console.log(statusText);
				console.log(errorThrown);
			}
		});
	});	

	// show/hide extra info when clicking on the row.
	$('tr').click(function() {
	    $(this).closest('tr').next('tr').toggle(400);
	});
});

