$(document).ready( function () {

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

