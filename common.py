# coding: utf8

ALLOWED_CHARACTERS = {'A', 'B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ENTER',
                      'ENT', 'ESCAPE', 'BSPACE', 'TAB', 'SPACE', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', '#',
                      '~', ';', ':', '‘', '"', '^', ',', '<', '.', '>', '/', '?', 'CAPS', 'F1', 'F2', 'F3', 'F4', 'F5',
                      'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19',
                      'F20', 'F21', 'F22', 'F23', 'F24', 'PRINT', 'SCROLL', 'PAUSE', 'INSERT', 'HOME', 'PGUP', 'DEL',
                      'END', 'PGDOWN', 'RIGHT', 'LEFT', 'UP', 'DOWN', 'NUM', 'KP_SLASH', 'KP_ASTERISK', 'KP_MINUS',
                      'KP_PLUS', 'KP_ENTER', 'KP_0', 'KP_1', 'KP_2', 'KP_3', 'KP_4', 'KP_5', 'KP_6', 'KP_7', 'KP_8', 'KP_9',
                      'KP_DOT', 'KP_EQUAL', 'LCTL', 'RCTL', 'LSFT', 'RSFT', 'LALT', 'FN11', 'FN12', 'FN13', 'FN14',
                      'FN15', 'FN16', 'FN17', 'FN18', 'FN19', 'FN20', 'FN21', 'FN22', 'FN23', 'FN24', 'FN25', 'FN26',
                      'FN27', 'FN28', 'FN29', 'FN30', 'FN31', 'TRNS', 'MSTP', 'MPLY', 'MPRV', 'MNXT', 'VOLU', 'VOLD', 'MUTE',
                      'PSCR', 'SLCK', 'MINUS', 'EQUAL', 'LBRACKET', 'RBRACKET', 'BSLASH', 'SCOLON', 'NONUS_HASH',
                      'QUOTE', 'GRV', 'COMMA', 'DOT', 'SLASH', 'DELETE', 'NLCK', 'RALT', 'LGUI', 'RGUI', 'FN0', 'FN1',
                      'FN2', 'ESC', 'FN3', 'FN4', 'FN5', 'FN6', 'FN7', 'FN8', 'FN9', 'FN10', '\'', 'APP'}

TRANSLATE_CHARACTERS = ['PRINT', 'SCROLL', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|',
                        '#', '~', ';', ':', '\'', '"', '`', ',', '<', '.', '>', '/', '?', 'DEL', 'NUM',
                        'LSHIFT', 'RSHIFT', 'LCTRL', 'RCTRL', 'MENU', 'KPSLASH', 'KPASTERISK', 'KPMINUS',
                        'KPPLUS', 'KPENTER', 'KP0', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8', 'KP9',
                        'KPDOT', 'KPEQUAL']

TRANSLATED_CHARACTERS = ['PSCR', 'SLCK', 'MINUS', 'MINUS', 'EQUAL', 'EQUAL', 'LBRACKET', 'LBRACKET', 'RBRACKET',
                         'RBRACKET', 'BSLASH', 'BSLASH', 'NONUS_HASH', 'NONUS_HASH', 'SCOLON', 'SCOLON', 'QUOTE',
                         'QUOTE', 'GRV', 'COMMA', 'COMMA', 'DOT', 'DOT', 'SLASH', 'SLASH', 'DELETE', 'NLCK',
                         'LSFT', 'RSFT', 'LCTL', 'RCTL', 'APP', 'KP_SLASH', 'KP_ASTERISK', 'KP_MINUS',
                         'KP_PLUS', 'KP_ENTER', 'KP_0', 'KP_1', 'KP_2', 'KP_3', 'KP_4', 'KP_5', 'KP_6', 'KP_7', 'KP_8', 'KP_9',
                         'KP_DOT', 'KP_EQUAL']

SHIFTED_CHARACTERS = ['|', '"', '_', '+', '{', '}', '<', '>', '?', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':']
UNSHIFTED_CHARACTERS=['BSLS','QUOT','MINS', 'EQL', 'LBRC', 'RBRC', 'COMM', 'DOT', 'SLSH', 'GRV', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'SCLN']


# Checks if a key is allowed (defined above)
def allowed_key(key):
    return key in ALLOWED_CHARACTERS


# Translated an already allowed key into its correct name required for TMK. If it's already correct, just return it back
def translate(key):
    if key in TRANSLATE_CHARACTERS:
        return TRANSLATED_CHARACTERS[TRANSLATE_CHARACTERS.index(key)]
    else:
        return key


# Takes a list of keys and translates them to all uppercase
def makeUpper(list):
    for i, val in enumerate(list):
        list[i] = list[i].upper()
    # print(list[i])
    return list


# Checks if an list of keys only contains allowed characters
def isAllowed(list):
    for i, val in enumerate(list):
        if not (list[i] in ALLOWED_CHARACTERS):
            return False
    return True


# Translated a list of keys with the translate function
def translateList(list):
    for i, val in enumerate(list):
        list[i] = translate(list[i])
    return list


# Takes all list and returns the TMK config file we need to compile the hex file
def createTemplate(function_actions, keymaps):
    with open("/app/tmk-modifications/keymap_template.c", "r") as templatefile:
        template = templatefile.read()

    template = template.replace("layers", keymaps, 1)
    template = template.replace("fnactions", function_actions, 1)

    return template

def buildKeyMaps(layers, template):

    keymaps = ''

    for layer in layers:
        layer_map = template
        layer_map = layer_map.format(*layer)

        keymaps += layer_map

    return keymaps

def fnActionLayer(fn_actions_list, l1, lt1, lm1):

    for i1, val1 in enumerate(lt1):
        if lt1[i1] == 'momentary' or lt1[i1] == 'toggle':
            layer = l1[i1]
            mode = 'MOMENTARY'
            if lt1[i1] == 'toggle':
                mode = 'TOGGLE'
            action = 'ACTION_LAYER_{0}({1}),'.format(mode, layer.split('L')[1])
            try:
                action_index = fn_actions_list.index(action)
            except ValueError:
                fn_actions_list.append(action)
                action_index = len(fn_actions_list) - 1

            l1[i1] = 'FN{0}'.format(action_index)

        elif lt1[i1] == 'tapkey':
            layer = lm1[i1]
            key = l1[i1]
            mode = 'MODS'
            prefix = 'MOD_'
            if len(layer) == 2:
                mode = 'LAYER'
                prefix = ''
                layer = layer.split('L')[1]
            action = 'ACTION_{0}_TAP_KEY({prefix}{1}, KC_{2}),'.format(mode, translate(layer), translate(key), prefix=prefix)
            try:
                action_index = fn_actions_list.index(action)
            except ValueError:
                fn_actions_list.append(action)
                action_index = len(fn_actions_list) - 1

            l1[i1] = 'FN{0}'.format(action_index)

        elif lt1[i1] == 'oneshot':
            key = l1[i1]
            action = 'ACTION_MODS_ONESHOT(MOD_{0}),'.format(translate(key))
            try:
                action_index = fn_actions_list.index(action)
            except ValueError:
                fn_actions_list.append(action)
                action_index = len(fn_actions_list) - 1

            l1[i1] = 'FN{0}'.format(action_index)

        elif lt1[i1] == 'setdefault':
            key = l1[i1]
            action = 'ACTION_DEFAULT_LAYER_SET({0}),'.format(key.split('L')[1])
            try:
                action_index = fn_actions_list.index(action)
            except ValueError:
                fn_actions_list.append(action)
                action_index = len(fn_actions_list) - 1

            l1[i1] = 'FN{0}'.format(action_index)

        elif lt1[i1] == 'setlayerclear':
            key = l1[i1]
            action = 'ACTION_LAYER_SET_CLEAR({0}),'.format(key.split('L')[1])
            try:
                action_index = fn_actions_list.index(action)
            except ValueError:
                fn_actions_list.append(action)
                action_index = len(fn_actions_list) - 1

            l1[i1] = 'FN{0}'.format(action_index)

        try:
            shift_index = SHIFTED_CHARACTERS.index(l1[i1])
        except ValueError:
            shift_index = -1
        if shift_index > -1:
            action = 'ACTION_MODS_KEY(MOD_LSFT, KC_{0}),'.format(UNSHIFTED_CHARACTERS[shift_index])
            try:
                action_index = fn_actions_list.index(action)
            except ValueError:
                fn_actions_list.append(action)
                action_index = len(fn_actions_list) - 1

            l1[i1] = 'FN{0}'.format(action_index)

        if l1[i1] == 'LED':
            action = 'ACTION_BACKLIGHT_STEP(),'
            try:
                action_index = fn_actions_list.index(action)
            except ValueError:
                fn_actions_list.append(action)
                action_index = len(fn_actions_list) - 1

            l1[i1] = 'FN{0}'.format(action_index)

    return fn_actions_list, l1

def buildFnActions(layers):

    fn_actions = ''
    fn_actions_list = []
    updated_layers = []

    for layer in layers:
        fn_actions_list, ulay = fnActionLayer(fn_actions_list, layer['values'], layer['types'], layer['mods'])
        updated_layers.append(ulay)

    for index, action in enumerate(fn_actions_list):
        fn_actions += '[{0}] = {1}'.format(index, action)

    fn_actions = fn_actions[:-1]
    return updated_layers, fn_actions

class Keyboard(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description', '')
        self.layouts = kwargs.get('layouts')
        self.firmware_folder = kwargs.get('firmware_folder')
