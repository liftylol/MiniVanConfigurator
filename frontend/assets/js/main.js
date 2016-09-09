/**
 * Calculates the absolute offset of the provided element
 */
cumulativeOffset = function(element) {
  var top = element.offsetHeight;
  var left = 0;

  // Continue looping through elements to build total offset
  do {
    top += element.offsetTop  || 0;
    left += element.offsetLeft || 0;
    element = element.offsetParent;
  } while(element);

  return {
    top: top,
    left: left
  };
};

/**
 * Creates a new template layer based on provided layout
 */
addLayer = function(layout) {
  var layers = [];

  for (var i = 0; i < layout.length; i++) {
    layers[i] = [];

    for (var j = 0; j < layout[i].length; j++) {
      layers[i][j] = {
        value: 'TRNS',
        type: null
      };
    };
  };

  return layers;
};

var v = new Vue({
  el: '#keyboard-form',
  data: {
    layout: layouts[0]['keys'],
    template: templates[0]['keys']
  },
  methods: {
    /**
     * Show right click menu
     */
    showMenu: function(event) {
      event.preventDefault();

      // Get current key and it's position'
      var key = event.srcElement;
      var position = cumulativeOffset(key);

      // Set the position of the tooltip and show it
      document.getElementById('key-list').style.top = position.top + 'px';
      document.getElementById('key-list').style.left = position.left + 'px';
      document.getElementById('key-list').style.display = 'block';
    },

    /**
     * Hide right click menu
     */
    hideMenu: function(event) {
      document.getElementById('key-list').style.display = 'none';
    },

    /**
     * Adds a new layer to the keyboard configuration
     */
    addLayer: function(event) {
      event.preventDefault();

      // @TODO: Limiting users at 15 total layers, can change if we want
      if (this.template.length < 15) {
        this.template.push(addLayer(this.layout));
      } else {
        alert('Cannot add any more layers.')
      }
    },

    /**
     * Removes the selected layer from the keyboard configuration
     *
     * @TODO: Figure out how to search array by reference (layer), passing ID too is dumb
     */
    removeLayer: function (event, layer, id) {
      event.preventDefault();

      if (id > 0) {
        delete this.template.$remove(layer);
      } else {
        alert('Cannot delete base layer');
      }
    }
  }
});