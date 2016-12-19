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
                      'KPDOT', 'KPEQUAL', 'LCTRL', 'RCTRL', 'LSHIFT', 'RSHIFT', 'LALT', 'FN11', 'FN12', 'FN13', 'FN14',
                      'FN15', 'FN16', 'FN17', 'FN18', 'FN19', 'FN20', 'FN21', 'FN22', 'FN23', 'FN24', 'FN25', 'FN26',
                      'FN27', 'FN28', 'FN29', 'FN30', 'FN31', 'TRNS', 'MSTP', 'MPLY', 'MPRV', 'MNXT', 'VOLU', 'VOLD',
                      'PSCR', 'SLCK', 'MINUS', 'EQUAL', 'LBRACKET', 'RBRACKET', 'BSLASH', 'SCOLON', 'NONUS_HASH',
                      'QUOTE', 'GRV', 'COMMA', 'DOT', 'SLASH', 'DELETE', 'NLCK', 'RALT', 'LGUI', 'RGUI', 'FN0', 'FN1',
                      'FN2', 'ESC', 'FN3', 'FN4', 'FN5', 'FN6', 'FN7', 'FN8', 'FN9', 'FN10', '\''}

TRANSLATE_CHARACTERS = ['PRINT', 'SCROLL', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|',
                        '#', '~', ';', ':', '\'', '"', '`', ',', '<', '.', '>', '/', '?', 'DEL', 'NUM']

TRANSLATED_CHARACTERS = ['PSCR', 'SLCK', 'MINUS', 'MINUS', 'EQUAL', 'EQUAL', 'LBRACKET', 'LBRACKET', 'RBRACKET',
                         'RBRACKET', 'BSLASH', 'BSLASH', 'NONUS_HASH', 'NONUS_HASH', 'SCOLON', 'SCOLON', 'QUOTE',
                         'QUOTE', 'GRV', 'COMMA', 'COMMA', 'DOT', 'DOT', 'SLASH', 'SLASH', 'DELETE', 'NLCK']
app = Flask(__name__)


# Returns the file to download at the very end
@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory("/app",
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
def createTemplate(list1, list2, list3, list4):
    with open("/app/tmk-modifications/keymap_tv44_template.c", "r") as templatefile:
        template = templatefile.read()

    for i1, val1 in enumerate(list1):
        template = template.replace("replace", list1[i1], 1)
    for i2, val2 in enumerate(list2):
        template = template.replace("replace", list2[i2], 1)
    for i3, val3 in enumerate(list3):
        template = template.replace("replace", list3[i3], 1)
    for i4, val4 in enumerate(list4):
        template = template.replace("replace", list4[i4], 1)

    return template


# This is our main routine. it allows GET and POST requests. If we get a GET request, we just send our template file
# to the browser (at the very end of the function) If it's a POST request, it means the browser already has our
# template and wants to send the values back to us. We do some sanity checks first to see if everything is ok The
# other steps we take will be explained right before everything.
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # as soon as we get a POST request we remember the current time so we can crank out tons of configs at and
        # every config has a unique name (1 request per second should be enough to not run into collisions at this
        # time i hope ;))
        now = str(datetime.datetime.now()).replace(' ', '-').replace(':', '-').split(".")[0]

        # Here we take all POST parameters and stuff them into lists. One layer has one list.
        layer1 = request.form.getlist('L1')
        layer2 = request.form.getlist('L2')
        layer3 = request.form.getlist('L3')
        layer4 = request.form.getlist('L4')

        # Each layer has to be exactly 44 entries long, check that first. If you leave a input box empty, the browser
        #  won't send the empty value at all. Plus if someone decided to use this as an API we check if he sends the
        # correct amount at of parameters first. If not, return an error.
        if (len(layer1) != 44) or (len(layer2) != 44) or (len(layer3) != 44) or (len(layer4) != 44):
            return 'error: some values are missing! please enter all information!'

        # At this point, we have all our intended keys stored. Next we have to convert them to uppercase to have
        # everything uniformly.
        layer1 = makeUpper(layer1)
        layer2 = makeUpper(layer2)
        layer3 = makeUpper(layer3)
        layer4 = makeUpper(layer4)

        # The next step is very important so we don't have incorrect, or even worse, malicious stuff in our files. We
        #  check if everything used is allowed. If not, return an error.
        if not (isAllowed(layer1) and isAllowed(layer2) and isAllowed(layer3) and isAllowed(layer4)):
            return 'error: there are invalid characters. please check your input!'

            # Now we translate all allowed keys into their real name required by the TMQ software. At this point,
        # all our data is already sanitized enough so we don't have to check for anything or throw errors because
        # there should not be any room for errors left :)
        layer1 = translateList(layer1)
        layer2 = translateList(layer2)
        layer3 = translateList(layer3)
        layer4 = translateList(layer4)

        # We can now insert all the values we got into the template file we use. This point can 'propably' be
        # improved still...
        configfile = createTemplate(layer1, layer2, layer3, layer4)

        # As soon as we have the entire content of our config, we can write it into a file (with the timestamp we
        # made right at the start!)
        filename = "keymap_tv44_" + now + ".c"
        callname = "tv44_" + now
        with open("/app/" + filename, "w+") as templatefile:
            templatefile.write(configfile)
            templatefile.close()

        # everything is set up, now we just have to make our hex file with a system call
        callstring = "make KEYMAP=" + callname + " TARGETFILE=" + callname + " > /dev/null"
        subprocess.call(callstring, shell=True, cwd="/_cut_/")

        # everything is done, we have to return the hex file! :)
        return redirect(url_for('download_file', filename=callname + '.hex'))

    # this is what happens on a GET request, we just send the index.htm file.
    else:
        return send_from_directory("/app/frontend/", "index.html")

# we enable the stuff below if we want to test locally
# app.debug = True
# app.run(host='localhost', port=18000)
