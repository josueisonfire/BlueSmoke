$(document).ready(function() {

	$.ajax({
		url: '/getStudentData',
		data: "{}",
		dataType: "json",
		success: function (data) {
			//console.log(data);
			//data = $.parseJSON(data);
			$.each(data, function(i, item) {
				$('#roster tr:last').after('<tr>' +
						'<td>' + item.FirstName + '</td>' +
						'<td>' + item.LastName + '</td>' +
						'<td>' + item.sID + '</td>' +
						'<td>' + item.fID + '</td>' +
																		'</tr>');
			});
		},
		error: function (response) {
				console.log(response);
		}
	});	
});