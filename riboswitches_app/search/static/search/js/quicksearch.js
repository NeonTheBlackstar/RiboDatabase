var Quicksearch = function() {

  return {


    init: function() {
      this.handleTwitterTypeahead();
    },


    handleTwitterTypeahead: function() {
        var LIMIT = 5
        var typeahead = $('#quicksearch');

        // Search 1
        var gene = new Bloodhound({
          datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.num); },
          queryTokenizer: Bloodhound.tokenizers.whitespace,
          remote: {
            url: ROOT_URL + 'genes?term=%QUERY&limit='+LIMIT,
            wildcard: '%QUERY'
           },
          limit: LIMIT
        });
        gene.initialize();
         
        // Search 2 
        var lig = new Bloodhound({
          datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.num); },
          queryTokenizer: Bloodhound.tokenizers.whitespace,
          remote: {
            url: ROOT_URL + 'ligands?term=%QUERY&limit='+LIMIT,
            wildcard: '%QUERY'
           },
          limit: LIMIT
        });     
        lig.initialize();

        // Search 3 
        var org = new Bloodhound({
          datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.num); },
          queryTokenizer: Bloodhound.tokenizers.whitespace,
          remote: {
            url: ROOT_URL + 'organisms?term=%QUERY&limit='+LIMIT,
            wildcard: '%QUERY'
           },
          limit: LIMIT
        });   
        org.initialize();

        // Typeahead initialization
        typeahead.typeahead(null, {
            name: 'gene',
            displayKey: 'name',
            source: gene.ttAdapter(),
            templates: {
                empty: [
                    '<div class="empty-message" style="padding-left: 20px; font-size="16px";>',
                    'No Results',
                    '</div>'
                ].join('\n'),
                header: '<h4 class="tt-header search-header">Genes</h4>'
            }
        },
        {
            name: 'org',
            displayKey: 'name',
            source: org.ttAdapter(),
            templates: {
                empty: [
                    '<div class="empty-message" style="padding-left: 20px; font-size="16px";>',
                    'No Results',
                    '</div>'
                ].join('\n'),
                header: '<h4 class="tt-header search-header">Organisms</h4>'
            }
        },
        {
            name: 'lig',
            displayKey: 'name',
            source: lig.ttAdapter(),
            templates: {
                empty: [
                    '<div class="empty-message" style="padding-left: 20px; font-size="16px";>',
                    'No Results',
                    '</div>'
                ].join('\n'),
                header: '<h4 class="tt-header search-header">Ligands</h4>'
            }
        });

       var numSelectedHandler = function (eventObject, suggestionObject, suggestionDataset) {
         location.href = suggestionObject.url;
       };
       typeahead.on('typeahead:selected', numSelectedHandler)

    }


  }

}();