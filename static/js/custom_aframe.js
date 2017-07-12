// Doby & Kieran


AFRAME.registerComponent('log', {
    schema: {type: 'string'},
    init: function () {
        let stringToLog = this.data;
        console.log(stringToLog);
    }
});


AFRAME.registerComponent('change-scale-on-hover', {
    schema: {
        scale: {default: '.4 .4 .4'}
    },
    init: function () {
        let data = this.data;
        let el = this.el;  // Scales collada-model="#simplex"
        let defaultScale = el.getAttribute('scale');

        el.addEventListener('mouseenter', function () {
            el.setAttribute('scale', '0.8 0.8 0.8');
            el.setAttribute('easing', 'ease-in');
            // Pause orbit (DOM traversal technique)
            // jQuery(this).parents('a-entity[id=orbit]').siblings('a-animation[class=revolution]');
        });
        el.addEventListener('mouseleave', function () {
            el.setAttribute('scale', defaultScale );
            el.setAttribute('easing', 'ease-in')
            // Resume orbit
        });
        el.addEventListener('click', function () {
            el.setAttribute('click',  );
        });
    }
});