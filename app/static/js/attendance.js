$(document).ready(function() {

	$.ajax({
		url: '/getAttendanceData',
		data: "{}",
		dataType: "json",
		success: function (data) {
			//data = $.parseJSON(data);
			$.each(data, function(i, item) {
				$('#attendance tr:last').after('<tr>' +
					 	'<td>' + item.FirstName + '</td>' +
						'<td>' + item.LastName + '</td>' +
						'<td>' + item.sID + '</td>' +
						'<td>' + item.Day1 + '</td>' +
						'<td>' + item.Day2 + '</td>' +
					 	'<td>' + item.Day3 + '</td>' +
					 	'<td>' + item.Day4 + '</td>' +
					 	'<td>' + item.Day5 + '</td>' +
					 	'<td>' + item.Day6 + '</td>' +
					 	'<td>' + item.Day7 + '</td>' +
																		'</tr>');
			});
		},
		error: function (response) {
				console.log(response);
		}
	});	
});