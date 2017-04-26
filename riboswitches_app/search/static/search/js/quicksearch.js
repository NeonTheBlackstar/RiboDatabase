var Quicksearch = function() {

  return {


    init: function() {
      this.handleTwitterTypeahead();
    },


    handleTwitterTypeahead: function() {
        var LIMIT = 5
        var typeahead = $('#quicksearch');

        // Search 1
        var ribo = new Bloodhound({
          datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.num); },
          queryTokenizer: Bloodhound.tokenizers.whitespace,
          remote: {
            url: ROOT_URL + 'riboswitches?term=%QUERY&limit='+LIMIT,
            wildcard: '%QUERY'
           },
          limit: LIMIT
        });
        ribo.initialize();
         
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

        // Typeahead initialization
        typeahead.typeahead(null, {
            name: 'ribo',
            displayKey: 'name',
            source: ribo.ttAdapter(),
            templates: {
                empty: [
                    '<h4 class="tt-header search-header">Riboswitches</h4>',
                    '<div class="empty-message">',
                    'No Results',
                    '</div>'
                ].join('\n'),
                header: '<h4 class="tt-header search-header">Riboswitches</h4>'
            }
        },
        {
            name: 'lig',
            displayKey: 'name',
            source: lig.ttAdapter(),
            templates: {
                empty: [
                    '<h4 class="tt-header search-header">Ligands</h4>',
                    '<div class="empty-message">',
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