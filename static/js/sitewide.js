jQuery(document).ready(function() {


    /* Next part of code handles hovering effect and submenu appearing */
    jQuery('.nav li').hover(
          function () {                      //appearing on hover
              jQuery('ul', this).fadeIn();
          },
          function () {                      //disappearing on hover
              jQuery('ul', this).fadeOut();
          });
    });

});