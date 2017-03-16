$(document).ready( function () {
	$('#ligand-table').DataTable(); //initialize dataTables
    $(".dropdown-toggle").dropdown(); //force bootstrap dropdown to work

    $(function () {
	  // create an instance when the DOM is ready
	  $('#jstree').jstree();
	});

} );
