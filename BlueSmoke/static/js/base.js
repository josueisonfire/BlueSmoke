$( document ).ready(function() {
					var index = 0;
					
					$.ajax({
						url: '/getTab',
						data: { Tab: index },
						type: 'GET',
						dataType: 'html',
						success: function (data) {
							$(data).insertAfter("#tabs");
						},
						error: function (response) {
							console.log(response);
						}
					});
				});
				
				
				$("li").on("click", function(){
					$("li").removeClass('active');
					$(this).addClass('active');
					
					$.ajax({
						url: '/getTab',
						data: { Tab: $(this).index() },
						type: 'GET',
						dataType: 'html',
						success: function (data) {
							$("#tabs").nextAll().remove();
							$(data).insertAfter("#tabs");
						},
						error: function (response) {
							console.log(response);
						}
					});
				});