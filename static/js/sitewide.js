// Doby & Kieran


jQuery(document).ready(function () {
    "use strict";

    // jQuery('code').on('keyup', function(evt){
    //     hljs.initHighlightingOnLoad();
    // });



    jQuery.ajax({
        url: 'https://coinmarketcap-nexuist.rhcloud.com/api/eth',
        method: 'GET',
        success: function (response){
            console.log(response.price.chf);
            jQuery('#CHF').text(Math.round(response.price.chf * 100) / 100);
            console.log(response.price.eur);
            jQuery('#EUR').text(Math.round(response.price.eur * 100) / 100);
            console.log(response.price.jpy);
            jQuery('#JPY').text(Math.round(response.price.jpy * 100) / 100);
            console.log(response.price.usd);
            jQuery('#USD').text(Math.round(response.price.usd * 100) / 100);

        }

    });


});