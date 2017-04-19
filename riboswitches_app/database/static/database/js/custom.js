$(document).ready( function () {

    $(".dropdown-toggle").dropdown(); //force bootstrap dropdown to work
    
    $(".panel-collapse").on("hide.bs.collapse", function () {
        $(".panel-collapse-clickable").find('i').removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
    });

    $(".panel-collapse").on("show.bs.collapse", function () {
        $(".panel-collapse-clickable").find('i').removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
    });

    $('main').removeClass('fade-out');


    $('.ligand-container').isotope({
        itemSelector: '.item',
        layoutMode: 'fitRows'
    });
     
    $('.ligand-filter ul li').click(function(){
        var selector = $(this).attr('data-filter'); 
        $('.ligand-container').isotope({ 
            filter: selector,  
        }); 
        return false; 
    }); 
} );

