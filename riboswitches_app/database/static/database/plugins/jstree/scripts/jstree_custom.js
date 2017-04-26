$(document).ready( function () {

    $(function () {

	 	$('#jstree-class').jstree({
			"types" : {
	      	"default" : {
            	    "icon" : "/static/database/images/folder-24.png"
            	},
            	"folder-open" : {
                	"icon" : "/static/database/images/open-folder-24.png"
            	},
	    	},
	    	"plugins" : [ "types", ]

	  	});

	 	//Fire up hyperlink in jstree
	  	$('#jstree-class').on("select_node.jstree", function (e, data) {
           document.location = data.instance.get_node(data.node, true).children('a').attr('href');
        });

		$("#jstree-class").on('open_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'folder-open');
		});
		$("#jstree-class").on('close_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'default');
		});


		$("#jstree-organism").on('open_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'folder-open');
		});
		$("#jstree-organism").on('close_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'default');
		});

	});

} );
