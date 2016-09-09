layouts = [
  {
    name: 'standard',
    keys: [
      [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 175],
      [125, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150],
      [175, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
      [125, 150, 125, 225, 200, 125, 150, 175]
    ]
  },
  {
    name: 'arrow',
    keys: [
      [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 175],
      [125, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150],
      [175, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
      [125, 150, 125, 225, 200, 150, 100, 100, 100]
    ]
  },
];

templates = [
  {
    name: 'standard',
    keys: [
      [
        [
          { value: 'TAB', type: null },
          { value: 'Q', type: null },
          { value: 'W', type: null },
          { value: 'E', type: null },
          { value: 'R', type: null },
          { value: 'T', type: null },
          { value: 'Y', type: null },
          { value: 'U', type: null },
          { value: 'I', type: null },
          { value: 'O', type: null },
          { value: 'P', type: null },
          { value: 'BSPACE', type: null }
        ],
        [
          { value: 'FN0', type: 'momentary' },
          { value: 'A', type: null },
          { value: 'S', type: null },
          { value: 'D', type: null },
          { value: 'F', type: null },
          { value: 'G', type: null },
          { value: 'H', type: null },
          { value: 'J', type: null },
          { value: 'K', type: null },
          { value: 'L', type: null },
          { value: ';', type: null },
          { value: 'FN0', type: 'momentary' }
        ],
        [
          { value: 'LSHIFT', type: null },
          { value: 'Z', type: null },
          { value: 'X', type: null },
          { value: 'C', type: null },
          { value: 'V', type: null },
          { value: 'B', type: null },
          { value: 'N', type: null },
          { value: 'M', type: null },
          { value: ',', type: null },
          { value: '.', type: null },
          { value: '/', type: null },
          // { value: 'FN1', type: 'momentary' }
        ],
        [
          { value: 'LCTRL', type: null },
          { value: 'FN1', type: 'momentary' },
          { value: 'LGUI', type: null },
          { value: 'ENTER', type: null },
          { value: 'SPACE', type: null },
          { value: 'RALT', type: null },
          { value: 'RSHIFT', type: null },
          { value: 'FN2', type: 'toggle' }
        ]
      ],
      [
        [
          { value: 'GRV', type: null },
          { value: 'FN4', type: null },
          { value: 'FN5', type: null },
          { value: 'FN6', type: null },
          { value: 'FN7', type: null },
          { value: 'FN8', type: null },
          { value: 'FN9', type: null },
          { value: 'FN10', type: null },
          { value: 'FN11', type: null },
          { value: 'FN12', type: null },
          { value: 'FN13', type: null },
          { value: 'DEL', type: null }
        ],
        [
          { value: 'FN0', type: null },
          { value: '\\', type: null },
          { value: '\'', type: null },
          { value: '-', type: null },
          { value: '=', type: null },
          { value: '{', type: null },
          { value: '}', type: null },
          { value: 'DOWN', type: null },
          { value: 'UP', type: null },
          { value: 'LEFT', type: null },
          { value: 'RIGHT', type: null },
          { value: 'FN0', type: null }
        ],
        [
          { value: 'TRNS', type: null },
          { value: 'ESC', type: null },
          { value: 'FN20', type: null },
          { value: 'PRINT', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'MSTP', type: null },
          { value: 'MPLY', type: null },
          { value: 'MPRV', type: null },
          { value: 'MNXT', type: null },
          { value: 'RSHIFT', type: null }
        ],
        [
          { value: 'TRNS', type: null },
          { value: 'LGUI', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null }
        ]
      ],
      [
        [
          { value: 'FN3', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: '7', type: null },
          { value: '8', type: null },
          { value: '9', type: null },
          { value: '0', type: null },
          { value: 'TRNS', type: null }
        ],
        [
          { value: 'ESC', type: null },
          { value: 'FN14', type: null },
          { value: 'FN15', type: null },
          { value: 'FN16', type: null },
          { value: 'FN17', type: null },
          { value: 'FN18', type: null },
          { value: 'FN19', type: null },
          { value: '4', type: null },
          { value: '5', type: null },
          { value: '6', type: null },
          { value: 'VOLU', type: null },
          { value: 'ENTER', type: null }
        ],
        [
          { value: 'FN1', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: '0', type: null },
          { value: '1', type: null },
          { value: '2', type: null },
          { value: '3', type: null },
          { value: 'VOLD', type: null },
          { value: 'FN1', type: null }
        ],
        [
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null }
        ]
      ],
      [
        [
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'F1', type: null },
          { value: 'F2', type: null },
          { value: 'F3', type: null },
          { value: 'F4', type: null },
          { value: 'TRNS', type: null }
        ],
        [
          { value: 'ESC', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'F5', type: null },
          { value: 'F6', type: null },
          { value: 'F7', type: null },
          { value: 'F8', type: null },
          { value: 'ENTER', type: null }
        ],
        [
          { value: 'LSHIFT', type: null },
          { value: '1', type: null },
          { value: '2', type: null },
          { value: '3', type: null },
          { value: '4', type: null },
          { value: '5', type: null },
          { value: '6', type: null },
          { value: 'F9', type: null },
          { value: 'F10', type: null },
          { value: 'F11', type: null },
          { value: 'F12', type: null },
          { value: 'RSHIFT', type: null }
        ],
        [
          { value: 'TRNS', type: null },
          { value: 'LSHIFT', type: null },
          { value: 'B', type: null },
          { value: 'SPACE', type: null },
          { value: 'C', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null },
          { value: 'TRNS', type: null }
        ]
      ]
    ]
  }
];


var Keyboard = (function () {
  function Keyboard(layout, template) {
    this.layout = layout;
    this.template = template;

    this.defaultKey = 'TRNS';
  }

  Keyboard.prototype.cumulativeOffset = function(element) {
    var top = element.offsetHeight,
      left = 0;

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

  Keyboard.prototype.createLayer = function(layout, layerTemplate) {
    var keyboard = document.createElement('div');
    keyboard.classList.add('keyboard');

    for (var i = 0; i < layout.length; i++) {
      var rowTemplate = null;
      if (typeof layerTemplate[i] !== 'undefined') {
        rowTemplate = layerTemplate[i];
      }

      var row = this.createRow(layout[i], rowTemplate);

      keyboard.appendChild(row);
    }

    return keyboard;
  }

  Keyboard.prototype.createRow = function(rowLayout, rowTemplate) {
    var row = document.createElement('div');
    row.classList.add('keyboard--row');

    for (var i = 0; i < rowLayout.length; i++) {
      var keyTemplate = null;
      if (typeof rowTemplate[i] !== 'undefined') {
        keyTemplate = rowTemplate[i];
      }

      var key = this.createKey(rowLayout[i], keyTemplate);

      row.appendChild(key);
    }

    return row;
  }

  Keyboard.prototype.createKey = function (keyLayout, keyTemplate) {
    var key = document.createElement('input');
    key.classList.add('keyboard--key', 'keyboard--key__' + keyLayout);

    if (keyTemplate !== null) {
      key.value = keyTemplate.value;
    } else {
      key.value = this.defaultKey;
    }

    key.name = 'L3';
    key.type = 'text';

    var that = this;

    key.addEventListener('contextmenu', function(e) {
      e.preventDefault();

      var key = e.srcElement;
      var position = that.cumulativeOffset(key);

      document.getElementById('key-list').style.top = position.top + 'px';
      document.getElementById('key-list').style.left = position.left + 'px';
      document.getElementById('key-list').style.display = 'block';
    }, false);

    key.addEventListener('blur', function (e) {
      document.getElementById('key-list').style.display = 'none';
    }, false);

    return key;
  }

  Keyboard.prototype.renderLayout = function() {
    var container = document.createElement('div');
    container.classList.add('keyboards');

    for (var i = 0; i < this.template.length; i++) {
      var keyboard = this.createLayer(this.layout, this.template[i]);

      container.appendChild(keyboard);
    }

    return container;
  };

  return Keyboard;
}());

// var layout = new Keyboard(layouts[0]['keys'], templates[0]['keys']).renderLayout();
// document.getElementById('keyboard-form').appendChild(layout);