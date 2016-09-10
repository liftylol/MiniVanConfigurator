buttonTypes = [
  {
    name: 'Normal',
    id: null,
  },
  {
    name: 'Toggle',
    id: 'toggle',
  },
  {
    name: 'Momentary',
    id: 'momentary',
  },
];

allowedCharacters = ['A', 'B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ENTER', 'ENT', 'ESCAPE', 'BSPACE', 'TAB', 'SPACE', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', '#', '~', ';', ':', '‘', '"', '^', ',', '<', '.', '>', '/', '?', 'CAPS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'PRINT', 'SCROLL', 'PAUSE', 'INSERT', 'HOME', 'PGUP', 'DEL', 'END', 'PGDOWN', 'RIGHT', 'LEFT', 'UP', 'DOWN', 'NUM', 'KPSLASH', 'KPASTERISK', 'KPMINUS', 'KPPLUS', 'KPENTER', 'KP0', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8', 'KP9', 'KPDOT', 'KPEQUAL', 'LCTRL', 'RCTRL', 'LSHIFT', 'RSHIFT', 'LALT', 'TRNS', 'MSTP', 'MPLY', 'MPRV', 'MNXT', 'VOLU', 'VOLD', 'PSCR', 'SLCK', 'MINUS', 'EQUAL', 'LBRACKET', 'RBRACKET', 'BSLASH', 'SCOLON', 'NONUS_HASH', 'QUOTE', 'GRV', 'COMMA', 'DOT', 'SLASH', 'DELETE', 'NLCK', 'RALT', 'LGUI', 'RGUI', 'ESC', 'FN0', 'FN1', 'FN2', 'FN3', 'FN4', 'FN5', 'FN6', 'FN7', 'FN8', 'FN9', 'FN10', 'FN11', 'FN12', 'FN13', 'FN14', 'FN15', 'FN16', 'FN17', 'FN18', 'FN19', 'FN20', 'FN21', 'FN22', 'FN23', 'FN24', 'FN25', 'FN26', 'FN27', 'FN28', 'FN29', 'FN30', 'FN31', 'PRINT', 'SCROLL', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', '#', '~', ';', ':', '\'', '"', '`', ',', '<', '.', '>', '/', '?', 'DEL', 'NUM'];

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
  el: 'body',
  data: {
    layout: layouts[0]['keys'],
    template: templates[0]['keys'],
    activeKey: null,
    buttonTypes: buttonTypes,
    allowedCharacters: allowedCharacters
  },
  methods: {
    /**
     * Build the classes required for the keyboard key container
     */
    keyContainerClasses(key, keyboard) {
      var classes = ['keyboard--key--container', 'keyboard--key--container__' + key.size];

      if (typeof keyboard !== 'undefined') {
        if (keyboard.type == 'toggle') {
          classes.push('keyboard--key--container__toggle');
        } else if (keyboard.type == 'momentary') {
          classes.push('keyboard--key--container__momentary');
        }
      }

      return classes;
    },

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
    },

    focusKey: function(key) {
      this.activeKey = key;
    }
  }
});