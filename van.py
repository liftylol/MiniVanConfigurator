# coding: utf8
import os, subprocess, datetime, fileinput
from flask import Flask, flash, request, redirect, url_for, send_from_directory

ALLOWED_CHARACTERS = {'A', 'B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ENTER',
                      'ENT', 'ESCAPE', 'BSPACE', 'TAB', 'SPACE', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', '#',
                      '~', ';', ':', '‘', '"', '^', ',', '<', '.', '>', '/', '?', 'CAPS', 'F1', 'F2', 'F3', 'F4', 'F5',
                      'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19',
                      'F20', 'F21', 'F22', 'F23', 'F24', 'PRINT', 'SCROLL', 'PAUSE', 'INSERT', 'HOME', 'PGUP', 'DEL',
                      'END', 'PGDOWN', 'RIGHT', 'LEFT', 'UP', 'DOWN', 'NUM', 'KPSLASH', 'KPASTERISK', 'KPMINUS',
                      'KPPLUS', 'KPENTER', 'KP0', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8', 'KP9',
                      'KPDOT', 'KPEQUAL', 'LCTL', 'RCTL', 'LSFT', 'RSFT', 'LALT', 'FN11', 'FN12', 'FN13', 'FN14',
                      'FN15', 'FN16', 'FN17', 'FN18', 'FN19', 'FN20', 'FN21', 'FN22', 'FN23', 'FN24', 'FN25', 'FN26',
                      'FN27', 'FN28', 'FN29', 'FN30', 'FN31', 'TRNS', 'MSTP', 'MPLY', 'MPRV', 'MNXT', 'VOLU', 'VOLD',
                      'PSCR', 'SLCK', 'MINUS', 'EQUAL', 'LBRACKET', 'RBRACKET', 'BSLASH', 'SCOLON', 'NONUS_HASH',
                      'QUOTE', 'GRV', 'COMMA', 'DOT', 'SLASH', 'DELETE', 'NLCK', 'RALT', 'LGUI', 'RGUI', 'FN0', 'FN1',
                      'FN2', 'ESC', 'FN3', 'FN4', 'FN5', 'FN6', 'FN7', 'FN8', 'FN9', 'FN10', '\'', 'APP'}

TRANSLATE_CHARACTERS = ['PRINT', 'SCROLL', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|',
                        '#', '~', ';', ':', '\'', '"', '`', ',', '<', '.', '>', '/', '?', 'DEL', 'NUM',
                        'LSHIFT', 'RSHIFT', 'LCTRL', 'RCTRL', 'MENU']

TRANSLATED_CHARACTERS = ['PSCR', 'SLCK', 'MINUS', 'MINUS', 'EQUAL', 'EQUAL', 'LBRACKET', 'LBRACKET', 'RBRACKET',
                         'RBRACKET', 'BSLASH', 'BSLASH', 'NONUS_HASH', 'NONUS_HASH', 'SCOLON', 'SCOLON', 'QUOTE',
                         'QUOTE', 'GRV', 'COMMA', 'COMMA', 'DOT', 'DOT', 'SLASH', 'SLASH', 'DELETE', 'NLCK',
                         'LSFT', 'RSFT', 'LCTL', 'RCTL', 'APP']

SHIFTED_CHARACTERS = ['|', '"', '_', '+', '{', '}', '<', '>', '?', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':']
UNSHIFTED_CHARACTERS=['BSLS','QUOT','MINS', 'EQL', 'LBRC', 'RBRC', 'COMM', 'DOT', 'SLSH', 'GRV', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'SCLN']

app = Flask(__name__)


# Returns the file to download at the very end
@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory("/app/tmk_keyboard/keyboard/tv44",
                               filename)


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


# Takes all list (currently fixed 4) and returns the TMK config file we need to compile the hex file
def createTemplate(function_actions, keymaps, arrow_layout):
    if arrow_layout:
        with open("/app/tmk-modifications/keymap_tv44_arrow_template.c", "r") as templatefile:
            template = templatefile.read()
    else:
        with open("/app/tmk-modifications/keymap_tv44_template.c", "r") as templatefile:
            template = templatefile.read()

    template = template.replace("layers", keymaps, 1)
    template = template.replace("fnactions", function_actions, 1)

    return template

# Takes all list (currently fixed 4) and returns the TMK config file we need to compile the hex file
def createLedTemplate(led_layer):
    with open("/app/tmk-modifications/led_template.c", "r") as templatefile:
        template = templatefile.read()

    template = template.replace("ledlayer", led_layer, 1)

    return template

def buildKeyMaps(layers, arrow_layout):

    layout = 'KEYMAP'
    if arrow_layout:
        layout = 'KEYMAP_ARROW'

    keymaps = ''
    keymap_template = '{0}(replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,'.format(layout)
    keymap_template += 'replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,'
    keymap_template += 'replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,'
    if arrow_layout:
        keymap_template += 'replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace, replace),'
    else:
        keymap_template += 'replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace),'

    for layer in layers:
        layer_map = keymap_template
        for i1, val1 in enumerate(layer):
            layer_map = layer_map.replace("replace", layer[i1], 1)

        keymaps += layer_map

    return keymaps

def fnActionLayer(layer_count, fn_action_index, l1, lt1, lm1):

    fn_actions = ''

    for i1, val1 in enumerate(lt1):
        if lt1[i1] == 'momentary' or lt1[i1] == 'toggle':
            layer = l1[i1]
            mode = 'MOMENTARY'
            if lt1[i1] == 'toggle':
                mode = 'TOGGLE'
            fn_actions += '[{0}] = ACTION_LAYER_{1}({2}),'.format(fn_action_index, mode, layer.split('L')[1])
            l1[i1] = 'FN{0}'.format(fn_action_index)
            fn_action_index += 1
        elif lt1[i1] == 'tapkey':
            layer = lm1[i1]
            key = l1[i1]
            mode = 'MODS'
            prefix = 'MOD_'
            if len(layer) == 2:
                mode = 'LAYER'
                prefix = ''
                layer = layer.split('L')[1]
            fn_actions += '[{0}] = ACTION_{1}_TAP_KEY({prefix}{2}, KC_{3}),'.format(fn_action_index, mode, translate(layer), translate(key), prefix=prefix)
            l1[i1] = 'FN{0}'.format(fn_action_index)
            fn_action_index += 1

        try:
            shift_index = SHIFTED_CHARACTERS.index(l1[i1])
        except ValueError:
            shift_index = -1
        if shift_index > -1:
            fn_actions += '[{0}] = ACTION_MODS_KEY(MOD_LSFT, KC_{1}),'.format(fn_action_index, UNSHIFTED_CHARACTERS[shift_index])
            l1[i1] = 'FN{0}'.format(fn_action_index)
            fn_action_index += 1

        if l1[i1] == 'LED':
            fn_actions += '[{0}] = ACTION_LAYER_TOGGLE({1}),'.format(fn_action_index, layer_count)
            l1[i1] = 'FN{0}'.format(fn_action_index)
            fn_action_index += 1

    return fn_action_index, l1, fn_actions

def buildFnActions(layers):

    fn_action_index = 0
    fn_actions = ''
    layer_actions = ''
    updated_layers = []

    for layer in layers:
        fn_action_index, ulay, layer_actions = fnActionLayer(len(layers), fn_action_index, layer['values'], layer['types'], layer['mods'])
        fn_actions += layer_actions
        updated_layers.append(ulay)

    fn_actions = fn_actions[:-1]

    return updated_layers, fn_actions


# This is our main routine. it allows GET and POST requests. If we get a GET request, we just send our template file
# to the browser (at the very end of the function) If it's a POST request, it means the browser already has our
# template and wants to send the values back to us. We do some sanity checks first to see if everything is ok The
# other steps we take will be explained right before everything.
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        #as soon as we get a POST request we remember the current time so we can crank out tons of configs at and every config has a unique name (1 request per second should be enough
        #to not run into collisions at this time i hope ;))
        now = str(datetime.datetime.now()).replace(' ', '-').replace(':', '-').split(".")[0]

        #Here we take all POST parameters and stuff them into lists. One layer has one list.
        arrow_layout = (request.form.get('arrow', '') == 'true')
        print(arrow_layout)
        layer1 = request.form.getlist('L1')
        layer1types = request.form.getlist('LT1')
        layer1mods = request.form.getlist('LM1')
        layer2 = request.form.getlist('L2')
        layer2types = request.form.getlist('LT2')
        layer2mods = request.form.getlist('LM2')
        layer3 = request.form.getlist('L3')
        layer3types = request.form.getlist('LT3')
        layer3mods = request.form.getlist('LM3')
        layer4 = request.form.getlist('L4')
        layer4types = request.form.getlist('LT4')
        layer4mods = request.form.getlist('LM4')
        layer5 = request.form.getlist('L5')
        layer5types = request.form.getlist('LT5')
        layer5mods = request.form.getlist('LM5')
        layer6 = request.form.getlist('L6')
        layer6types = request.form.getlist('LT6')
        layer6mods = request.form.getlist('LM6')
        layer7 = request.form.getlist('L7')
        layer7types = request.form.getlist('LT7')
        layer7mods = request.form.getlist('LM7')

        layers = []
        if layer1:
            layers.append({'values': layer1, 'types': layer1types, 'mods': layer1mods})

        if layer2:
            layers.append({'values': layer2, 'types': layer2types, 'mods': layer2mods})

        if layer3:
            layers.append({'values': layer3, 'types': layer3types, 'mods': layer3mods})

        if layer4:
            layers.append({'values': layer4, 'types': layer4types, 'mods': layer4mods})

        if layer5:
            layers.append({'values': layer5, 'types': layer5types, 'mods': layer5mods})

        if layer6:
            layers.append({'values': layer6, 'types': layer6types, 'mods': layer6mods})

        if layer7:
            layers.append({'values': layer7, 'types': layer7types, 'mods': layer7mods})

        keys_per_layer = 44
        if arrow_layout:
            keys_per_layer = 45

        for layer in layers:
            if (len(layer['values']) != keys_per_layer):
                return('error: some values are missing! please enter all information!')

        layers, fn_actions = buildFnActions(layers)
        #print(fn_actions)

        for layer in layers:
            layer = makeUpper(layer)
            layer = translateList(layer)
            if not(isAllowed(layer)):
                return('error: there are invalid characters. please check your imput!<p>{0}</p>'.format(layer))

        keymaps = buildKeyMaps(layers, arrow_layout)
        #print(keymaps)

        #The next step is very important so we don't have incorrect, or even worse, malicious stuff in our files. We check if everything used is allowed. If not, return an error.
        if not (isAllowed(layer1) and isAllowed(layer2) and isAllowed(layer3) and isAllowed(layer4)):
            return('error: there are invalid characters. please check your input!')

        #We can now insert all the values we got into the template file we use. This point can 'propably' be improved still...
        configfile = createTemplate(fn_actions, keymaps, arrow_layout)
        ledconfigfile = createLedTemplate('{0}'.format(len(layers)))

        #As soon as we have the entire content of our config, we can write it into a file (with the timestamp we made right at the start!)
        filename = "keymap_tv44_"+now+".c"
        ledfilename = "led_"+now+".c"
        callname = "tv44_"+now
        ledname = "led_"+now
        with open("/app/tmk_keyboard/keyboard/tv44/"+filename, "w+") as templatefile:
            templatefile.write(configfile)
            templatefile.close()

        with open("/app/tmk_keyboard/keyboard/tv44/"+ledfilename, "w+") as templatefile:
            templatefile.write(ledconfigfile)
            templatefile.close()

        #everything is set up, now we just have to make our hex file with a system call
        callstring = "make KEYMAP="+callname+" TARGETFILE="+callname+" LEDCONF="+ledname+" > /dev/null"
        subprocess.call(callstring, shell=True, cwd="/app/tmk_keyboard/keyboard/tv44/")

        #everything is done, we have to return the hex file! :)
        return redirect(url_for('download_file', filename=callname+'.hex'))

    #this is what happens on a GET request, we just send the index.htm file.
    else:
        return send_from_directory("/app/frontend/", "index.html")
