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
  {
    name: 'Tap Key',
    id: 'tapkey'
  }
];

alphas = ['A', 'B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
standard_functions = ['ENTER', 'ENT', 'ESCAPE', 'BSPACE', 'TAB', 'SPACE', 'CAPS', 'PRINT', 'SCROLL', 'PAUSE', 'INSERT', 'HOME', 'PGUP', 'DEL', 'END', 'PGDOWN', 'RIGHT', 'LEFT', 'UP', 'DOWN', 'NONUS_HASH'];
special_characters = ['\\', '\'', '-', '=', '[', ']', ',', '.', '/', '`', ';'];
shifted_characters = ['|', '"', '_', '+', '{', '}', '<', '>', '?', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':'];
eff_keys = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24'];
numpad = ['NUM', 'KPSLASH', 'KPASTERISK', 'KPMINUS', 'KPPLUS', 'KPENTER', 'KP0', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8', 'KP9', 'KPDOT', 'KPEQUAL'];
modifiers = ['LCTRL', 'RCTRL', 'LSHIFT', 'RSHIFT', 'LALT', 'RALT', 'LGUI', 'RGUI'];
media = ['MSTP', 'MPLY', 'MPRV', 'MNXT', 'VOLU', 'VOLD'];
keyboard = ['TRNS', 'LED'];
duplicate_codes = ['PSCR', 'SLCK', 'MINUS', 'EQUAL', 'LBRACKET', 'RBRACKET', 'BSLASH', 'SCOLON', 'NONUS_HASH', 'QUOTE', 'GRV', 'COMMA', 'DOT', 'SLASH', 'DELETE', 'NLCK', 'RALT', 'ESC'];
layers = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7'];

allowedCharacters = alphas.concat(numbers);
allowedCharacters = allowedCharacters.concat(standard_functions);
allowedCharacters = allowedCharacters.concat(special_characters);
allowedCharacters = allowedCharacters.concat(shifted_characters);
allowedCharacters = allowedCharacters.concat(eff_keys);
allowedCharacters = allowedCharacters.concat(numpad);
allowedCharacters = allowedCharacters.concat(modifiers);
allowedCharacters = allowedCharacters.concat(media);
allowedCharacters = allowedCharacters.concat(keyboard);
modsAndLayers = modifiers.concat(layers);

var v = new Vue({
  el: 'body',
  data: {
    layout: layouts[0]['keys'], // Layout
    template: templates[0]['keys'], // Template
    activeKey: null, // Currently active key
    buttonTypes: buttonTypes, // List of button types
    allowedCharacters: allowedCharacters, // Allowed set of characters
    modsAndLayers: modsAndLayers,
    layers: layers,
    isLayer: false,
    isNotLayer: true,
    contextMenuVisible: false, // Show we be showing the context menu?
    tapKeyVisible: false,
    contextMenuPosition: { // Position of the context menu
      top: 0,
      left: 0
    },
    fnActionCount: 0,
    fnActionLimit: 32,
    arrow: false,
    layerLimit: 8 // Maximum number of layers
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
          this.tapKeyVisible = false;
          this.isLayer = true;
          this.isNotLayer = false;
        } else if (keyboard.type == 'momentary') {
          classes.push('keyboard--key--container__momentary');
          this.tapKeyVisible = false;
          this.isLayer = true;
          this.isNotLayer = false;
        } else if (keyboard.type == 'tapkey') {
          classes.push('keyboard--key--container__tapkey');
          this.tapKeyVisible = true;
          this.isLayer = false;
          this.isNotLayer = true;
        } else {
          this.isLayer = false;
          this.isNotLayer = true;
        }
      }

      return classes;
    },

    /**
     * Set the position of the context menu
     */
    positionContextMenu: function (event) {
      // Get current key and it's position'
      var key = event.srcElement;
      var position = this.cumulativeOffset(key);

      Vue.nextTick(function () {
        // Set the position of the tooltip and show it
        this.contextMenuPosition.top = position.top;
        this.contextMenuPosition.left = position.left;
      }.bind(this));
    },

    /**
     * Show context menu
     */
    showContextMenu: function(event) {
      event.preventDefault();

      this.contextMenuVisible = true;
      if (this.activeKey.type == 'tapkey') {
          this.tapKeyVisible = true;
      } else {
          this.tapKeyVisible = false;
      }
      if (this.activeKey.type == 'toggle' || this.activeKey.type == 'momentary') {
          this.isLayer = true;
          this.isNotLayer = false;
      } else {
          this.isLayer = false;
          this.isNotLayer = true;
      }
    },

    /**
     * Hide context menu
     */
    hideContextMenu: function (event) {
      var button = event.which || event.button;

      if (button === 1 && !this.clickInsideContextMenu(event)) {
        this.contextMenuVisible = false;
      }
    },

    /**
     * Check if the click is inside the context menu
     *
     * @returns boolean True if inside, false if outside
     */
    clickInsideContextMenu: function (event) {
      var element = event.srcElement || event.target;
      var className = 'context-menu';

      if ( element.classList.contains(className) ) {
        return element;
      } else {
        while ( element = element.parentNode ) {
          if ( element.classList && element.classList.contains(className) ) {
            return element;
          }
        }
      }

      return false;
    },

    /**
     * builds the hex file and returns it as a download
     */
    makeHex: function(event) {
        event.preventDefault();

        document.forms["keyboard-form"].submit();
    },

    /**
     * changes the layout
     */
    changeLayout: function(event) {
        event.preventDefault();

        if (this.arrow) {
            this.layout = layouts[0]['keys'];
            this.template = templates[0]['keys'];
            this.arrow = false;
        } else {
            this.layout = layouts[1]['keys'];
            this.template = templates[1]['keys'];
            this.arrow = true;
        }
    },

    /**
     * Adds a new layer to the keyboard configuration
     */
    addLayer: function(event) {
      event.preventDefault();

      // Limiting users at 33 total layers
      if (this.template.length < this.layerLimit) {
        this.template.push(this.createNewLayer(this.layout));
      } else {
        alert('Sorry, cannot add any more layers.')
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

    /**
     * Set the active key and reposition the context menu
     */
    focusKey: function(key, event) {
      this.activeKey = key;
      this.positionContextMenu(event);
    },

    /**
     * Calculates the absolute offset of the provided element
     */
    cumulativeOffset: function(element) {
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
    },

    /**
     * Creates a new template layer based on provided layout
     */
    createNewLayer: function(layout) {
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
    }
  }
});
