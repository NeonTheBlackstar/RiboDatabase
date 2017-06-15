function get_records() {
	$.ajax({
		data: {
			term: $('input[name="term"]').val()
		},
		url: '/searcher/results/',
		success: function(json) {
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
			$('#records').html(html);
		},
		error : function(xhr,errmsg,err) {
            alert("Error");
        }
	});
}

$(document).ready( function () {
	$('#search_records').on('click', function(e) {
		e.preventDefault();
		get_records();
	})
});