keyboards = [];
keyboards.push({'name':'minivan_rev1', 'layouts':minivan_layouts, 'templates':minivan_templates});
keyboards.push({'name':'roadkit', 'layouts':roadkit_layouts, 'templates':roadkit_templates});
keyboards.push({'name':'transitvan', 'layouts':transitvan_layouts, 'templates':transitvan_templates});
keyboards.push({'name':'cargovan', 'layouts':cargovan_layouts, 'templates':cargovan_templates});
keyboards.push({'name':'provan', 'layouts':provan_layouts, 'templates':provan_templates});
keyboards.push({'name':'minorca', 'layouts':minorca_layouts, 'templates':minorca_templates});
keyboards.push({'name':'ergodox', 'layouts':ergodox_layouts, 'templates':ergodox_templates});

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
  },
  {
    name: 'One Shot Modifier',
    id: 'oneshot'
  },
  {
    name: 'Set Layer Clear',
    id: 'setlayerclear'
  },
  {
    name: 'Set Default Layer',
    id: 'setdefault'
  }
];

alphas = ['A', 'B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
standard_functions = ['ENTER', 'ENT', 'ESCAPE', 'BSPACE', 'TAB', 'SPACE', 'CAPS', 'PRINT', 'SCROLL', 'PAUSE', 'INSERT', 'HOME', 'PGUP', 'DEL', 'END', 'PGDOWN', 'RIGHT', 'LEFT', 'UP', 'DOWN', 'NONUS_HASH'];
special_characters = ['\\', '\'', '-', '=', '[', ']', ',', '.', '/', '`', ';'];
shifted_characters = ['|', '"', '_', '+', '{', '}', '<', '>', '?', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':'];
eff_keys = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24'];
numpad = ['NUM', 'KPSLASH', 'KPASTERISK', 'KPMINUS', 'KPPLUS', 'KPENTER', 'KP0', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8', 'KP9', 'KPDOT', 'KPEQUAL', 'MENU'];
modifiers = ['LCTRL', 'RCTRL', 'LSHIFT', 'RSHIFT', 'LALT', 'RALT', 'LGUI', 'RGUI'];
media = ['MSTP', 'MPLY', 'MPRV', 'MNXT', 'VOLU', 'VOLD', 'MUTE'];
keyboard = ['TRNS', 'LED', 'FLASH'];
duplicate_codes = ['PSCR', 'SLCK', 'MINUS', 'EQUAL', 'LBRACKET', 'RBRACKET', 'BSLASH', 'SCOLON', 'NONUS_HASH', 'QUOTE', 'GRV', 'COMMA', 'DOT', 'SLASH', 'DELETE', 'NLCK', 'RALT', 'ESC'];
layers = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15'];
base_layer = ['L0'];

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
tapKeys = alphas.concat(numbers);
tapKeys = tapKeys.concat(standard_functions);
tapKeys = tapKeys.concat(special_characters);
tapKeys = tapKeys.concat(numpad);
tapKeys = tapKeys.concat(eff_keys);
tapKeys = tapKeys.concat(media);
allLayers = base_layer.concat(layers);


function setInitialKeyboard() {
    var active_keyboard = localStorage.getItem('current-keyboard');
    if (active_keyboard) {
        for (var k in keyboards) {
            if (keyboards[k].name == active_keyboard) {
                return k;
            }
        }
    }

    return 0;
}

function setInitialKeymap() {
    var initial_keyboard = setInitialKeyboard();
    var k = keyboards[initial_keyboard];
    var keyboard_storage_name = 'user-keymap-' + k.name;
    var sKeymap = localStorage.getItem(keyboard_storage_name);
    if (sKeymap) {
        return JSON.parse(sKeymap)['keymap'];
    }

    return k.templates[0]['keys'];
}

function setInitialLayout() {
    var initial_keyboard = setInitialKeyboard();
    var k = keyboards[initial_keyboard];
    var keyboard_storage_name = 'user-keymap-' + k.name;
    var sKeymap = localStorage.getItem(keyboard_storage_name);

    if (sKeymap) {
        var keymap = JSON.parse(sKeymap);
        if (keymap.hasOwnProperty('activeLayout')) {
            return k.layouts[keymap.activeLayout]['keys'];
        } else {
            if (keymap['arrow']) {
                return k.layouts[1]['keys'];
            } else {
                return k.layouts[0]['keys'];
            }
        }
    }
}

function setInitialActiveLayout() {
    var initial_keyboard = setInitialKeyboard();
    var k = keyboards[initial_keyboard];
    var keyboard_storage_name = 'user-keymap-' + k.name;
    var sKeymap = localStorage.getItem(keyboard_storage_name);
    if (sKeymap) {
        var keymap = JSON.parse(sKeymap);
        if (keymap.hasOwnProperty('activeLayout')) {
            return JSON.parse(sKeymap)['activeLayout'];
        }
    }

    return 0;
}


var v = new Vue({
  el: 'body',
  data: {
    layout: setInitialLayout(), // Layout
    template: setInitialKeymap(), // Template
    activeKey: null, // Currently active key
    buttonTypes: buttonTypes, // List of button types
    allowedCharacters: allowedCharacters, // Allowed set of characters
    modsAndLayers: modsAndLayers,
    tapKeys : tapKeys,
    layers: layers,
    allLayers: allLayers,
    modifiers: modifiers,
    keyType: 'normal',
    contextMenuVisible: false, // Show we be showing the context menu?
    contextMenuPosition: { // Position of the context menu
      top: 0,
      left: 0
    },
    fnActionCount: 0,
    fnActionLimit: 32,
    supportedLayouts: keyboards[setInitialKeyboard()].layouts,
    activeLayout: setInitialActiveLayout(),
    layerLimit: 16, // Maximum number of layers
    keymapRaw: '',
    keyboards: keyboards,
    activeKeyboard: setInitialKeyboard()
  },
  created: function () {
    this.saveLayout();
  },
  methods: {
    /**
     * Build the classes required for the keyboard key container
     */
    keyContainerClasses(key, keyboard) {
      var classes = ['keyboard--key--container', 'keyboard--key--container__' + key.size];

      if (key.type == 'spacer') {
          classes.push('spacer');
      }

      if (typeof keyboard !== 'undefined') {
        if (keyboard.type == 'toggle') {
          classes.push('keyboard--key--container__toggle');
          this.keyType = 'layer';
        } else if (keyboard.type == 'momentary') {
          classes.push('keyboard--key--container__momentary');
          this.keyType = 'layer';
        } else if (keyboard.type == 'tapkey') {
          classes.push('keyboard--key--container__tapkey');
          this.keyType = 'tapkey';
        } else if (keyboard.type == 'oneshot') {
          classes.push('keyboard--key--container__oneshot');
          this.keyType = 'oneshot';
        } else if (keyboard.type == 'setdefault') {
          classes.push('keyboard--key--container__setdefault');
          this.keyType = 'setlayer';
        } else if (keyboard.type == 'setlayerclear') {
          classes.push('keyboard--key--container__setlayerclear');
          this.keyType = 'setlayer';
        } else {
          this.keyType = 'normal';
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

    buildKeymapJson: function () {
        var keyboard = {'keyboard':this.keyboards[this.activeKeyboard]['name'], 'activeLayout':this.activeLayout, 'keymap': []};
        var keymap = [];
        var layer = [];
        var row = [];
        var key = {};
        for (layerIndex in this.template) {
            layer = [];
            for (rowIndex in this.template[layerIndex]) {
                row = [];
                for (keyIndex in this.template[layerIndex][rowIndex]) {
                    var k = this.template[layerIndex][rowIndex][keyIndex]
                    key = {value: k.value, type: k.type, mod: k.mod};
                    row.push(key);
                }
                layer.push(row);
            }
            keymap.push(layer);
        }

        keyboard['keymap'] = keymap
        return JSON.stringify(keyboard);
    },

    saveLayout: function() {
        var sKeymap = this.buildKeymapJson();
        this.keymapRaw = sKeymap;
        var k = this.keyboards[this.activeKeyboard];
        var keyboard_storage_name = 'user-keymap-' + k.name;
        localStorage.setItem(keyboard_storage_name, sKeymap);
        localStorage.setItem('current-keyboard', k.name);
        this.fnActionCount = this.countFnActions();
    },

    readKeymapJson: function() {
        var keyboard = JSON.parse(document.getElementById("rawmap").value);

        // need to handle legacy maps
        if (Array.isArray(keyboard)) {
            this.template = keyboard;
        } else {
            if (keyboard.hasOwnProperty('keyboard')) {
                for (var k in this.keyboards) {
                    if (this.keyboards[k].name == keyboard['keyboard']) {
                        this.activeKeyboard = k;
                        this.supportedLayouts = this.keyboards[k].layouts;
                        break;
                    }
                }
            } else {
                this.activeKeyboard = 0;
            }
            if (keyboard.hasOwnProperty('activeLayout')) {
                this.layout = this.keyboards[this.activeKeyboard].layouts[keyboard['activeLayout']]['keys'];
                this.activeLayout = keyboard['activeLayout'];
            } else {
                if (keyboard['arrow']) {
                    this.layout = this.keyboards[this.activeKeyboard].layouts[1]['keys'];
                    this.activeLayout = 1;
                } else {
                    this.layout = this.keyboards[this.activeKeyboard].layouts[0]['keys'];
                    this.activeLayout = 0;
                }
            }
            this.template = keyboard['keymap'];
        }
        this.saveLayout();
    },

    resetToDefault: function() {
        this.template = this.keyboards[this.activeKeyboard].templates[this.activeLayout]['keys'];
        this.saveLayout();
    },

    countFnActions: function() {
        var fnActions = [];
        for (layerIndex in this.template) {
            for (rowIndex in this.template[layerIndex]) {
                for (keyIndex in this.template[layerIndex][rowIndex]) {
                    var k = this.template[layerIndex][rowIndex][keyIndex]
                    if (k.type === 'toggle' || k.type === 'momentary' || k.type === 'oneshot' || k.type === 'setlayerclear' || k.type === 'setdefault') {
                        if (fnActions.indexOf(k.type + k.value) < 0) {
                            fnActions.push(k.type + k.value);
                        }
                    } else if (k.type === 'tapkey') {
                        if (fnActions.indexOf(k.type + k.value + k.mod) < 0) {
                            fnActions.push(k.type + k.value + k.mod);
                        }
                    }

                    if (shifted_characters.indexOf(k.value) > -1) {
                        if (fnActions.indexOf(k.value) < 0) {
                            fnActions.push(k.value);
                        }
                    }

                    if (k.value === 'LED') {
                        if (fnActions.indexOf(k.value) < 0) {
                            fnActions.push(k.value);
                        }
                    }

                    if (k.value === 'FLASH') {
                        if (fnActions.indexOf(k.value) < 0) {
                            fnActions.push(k.value);
                        }
                    }
                }
            }
        }

        return fnActions.length;
    },

    /**
     * Show context menu
     */
    showContextMenu: function(event) {
      event.preventDefault();

      this.contextMenuVisible = true;
      if (this.activeKey.type == 'tapkey') {
          this.keyType = 'tapkey';
      } else if (this.activeKey.type == 'toggle' || this.activeKey.type == 'momentary') {
          this.keyType = 'layer';
      } else if (this.activeKey.type == 'oneshot') {
          this.keyType = 'oneshot';
      } else if (this.activeKey.type == 'setdefault' || this.activeKey.type == 'setlayerclear') {
          this.keyType = 'setlayer';
      } else {
          this.keyType = 'normal';
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

        this.layout = this.keyboards[this.activeKeyboard].layouts[this.activeLayout]['keys'];
        this.template = this.keyboards[this.activeKeyboard].templates[this.activeLayout]['keys'];
        this.saveLayout();
    },

    /**
     * changes the keyboard
     */
    changeKeyboard: function(event) {
        event.preventDefault();

        // load saved config other set Default
        var k = this.keyboards[this.activeKeyboard];
        var keyboard_storage_name = 'user-keymap-' + k.name;
        var sKeymap = localStorage.getItem(keyboard_storage_name);
        if (sKeymap) {
            var keymap = JSON.parse(sKeymap);
            this.template = keymap['keymap'];
            this.layout = k.layouts[keymap.activeLayout]['keys'];
            this.activeLayout = keymap['activeLayout'];
        } else {
            this.template = k.templates[0]['keys'];
            this.layout = k.layouts[0]['keys'];
            this.activeLayout = 0;
        }
        this.supportedLayouts = k.layouts;
        this.saveLayout();
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
