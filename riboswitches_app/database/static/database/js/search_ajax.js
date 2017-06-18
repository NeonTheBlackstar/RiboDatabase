function get_records() {

	// ajax function for displaying results without reloading page
	$.ajax({
		data: {
			term: $('input[name="term_ligand"]').val()
		},
		url: '/searcher/results/',
		beforeSend: function() {
			// adding loader
			$('#records').html('').addClass('loading');
		},
		success: function(json) {
			if(json.records.length != 0) {
				var html = '<div class="panel panel-default" id="panel-search-results">'
				for (var i=0; i < json.records.length; i++) {
					var riboswitch_name = json.records[i];
					html += '<a href="/search/record/';
					html += riboswitch_name;
					html += '">';
					html += '<div class="panel-body">';
					html += riboswitch_name;
					html += '</div>'
					html += '</a>'
				}
				html += '</div>'
				$('#records').html(html).removeClass('loading');
			}
			else {
				// if there is no results
				var html = '<div class="panel panel-default" id="panel-search-results">\
								<p id="no-results-msg">No results found</p>\
							</div>';
				$('#records').html(html).removeClass('loading');
			}
		},
		error : function(xhr,errmsg,err) {
            console.log(errmsg);
        }
	});
}

$(document).ready( function () {
	$('#search_records').on('click', function(e) {
		e.preventDefault();
		$('#records').addClass('loading').css('display', 'none');
		get_records();

		// animate appearing of the results
		$('#records').fadeIn("fast");
	});
});