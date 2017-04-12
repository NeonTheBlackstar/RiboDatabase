$(document).ready( function () {

    $(".dropdown-toggle").dropdown(); //force bootstrap dropdown to work
    
    $(".panel-collapse").on("hide.bs.collapse", function () {
        $(".panel-collapse-clickable").find('i').removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
    });

    $(".panel-collapse").on("show.bs.collapse", function () {
        $(".panel-collapse-clickable").find('i').removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
    });

    $('main').removeClass('fade-out');




    $(window).load(function(){
    var $container = $('.ligand-container');
    $container.isotope({
        animationOptions: {
            duration: 750,
            easing: 'linear',
            queue: false
        }
    });
 
    $('.ligand-filter a').click(function(){
 
        var selector = $(this).attr('data-filter'); 
        $container.isotope({ 
            filter: selector, 
            animationOptions: { 
                duration: 750, 
                easing: 'linear', 
                queue: false, 
            } 
        }); 
      return false; 
   		}); 
	});
} );

