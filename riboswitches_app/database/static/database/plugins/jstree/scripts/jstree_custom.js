$(document).ready( function () {

    $(function () {
	  // create an instance when the DOM is ready
	  $('#jstree-organism').jstree();

		$("#jstree-organism").on('open_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'folder-open');
		});
		$("#jstree-organism").on('close_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'default');
		});


	  $('#jstree-class').jstree({
		"types" : {
	      "default" : {
	        "icon" : "fa fa-folder-o"
	      },
	      "folder-open" : {
	      	"icon" : "fa fa-folder-open-o"
	      },
	    },
	    "plugins" : [ "types" ]

	  });

		$("#jstree-class").on('open_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'folder-open');
		});
		$("#jstree-class").on('close_node.jstree', function (event, data) {
    		data.instance.set_type(data.node,'default');
		});

	  // create an instance when the DOM is ready
	  

	});

} );
