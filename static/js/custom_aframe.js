// Doby & Kieran


AFRAME.registerComponent('log', {
    schema: {type: 'string'},

    init: function () {
        let stringToLog = this.data;
        console.log(stringToLog);
    }
});


// // Component to generate text on click.
// AFRAME.registerComponent('cursor-listener', {
//   init: function () {
//     this.el.addEventListener('click', function (evt) {
//       console.log('I was clicked at: ', evt.detail.intersection.point);
//     });
//   }
// });



/*fetch() allows you to make network requests similar to XMLHttpRequest (XHR).
The main difference is that the Fetch API uses Promises, which enables a simpler and cleaner API,
avoiding callback hell and having to remember the complex API of XMLHttpRequest.*/

// let myInit = { method: 'GET'};
//
// fetch("https://api.blockcypher.com/v1/eth/main", myInit).then(function(response) {
//    console.log(`${response.status}: ${response.statusText}`);
//    return response.json();
// }).then(function(data) {
//    console.log(data.high_gas_price);
//
// }).catch(function(error) {
//   console.log('Houston, there has been a problem.: ' + error.message);
// });

let entity = document.createElement('a-entity');
scene.appendChild(entity);
entity.setAttribute('position', { x: 0, y: 1, z: 2 });
entity.addEventListener('loaded', function() {
  console.log(entity.getAttribute('position'));
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
        // el.addEventListener('click', function () {
        //     el.setAttribute('',  );
        // });
    }
});