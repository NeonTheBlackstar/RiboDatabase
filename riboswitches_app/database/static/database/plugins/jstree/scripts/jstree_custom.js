$(document).ready( function () {

    $(function () {
	  // create an instance when the DOM is ready
	  $('#jstree').jstree({
		"types" : {
	      "default" : {
	        "icon" : "fa fa-folder"
	      },
	      "folder-open" : {
	      	"icon" : "fa fa-folder-open"
	      },
	    },
	    "plugins" : [ "types" ]

	  });

		$("#jstree").on('open_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'folder-open');
		});
		$("#jstree").on('close_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'default');
		});

	});

} );
