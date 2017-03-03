# coding: utf8
import os, subprocess, datetime, fileinput
from flask import Flask, flash, request, redirect, url_for, send_from_directory
import common as kbd

KEYBOARDS = []
# import keyboard configurations and add them to app keyboard list
from keyboards.minivan import keyboard as minivan_rev1
KEYBOARDS.append(minivan_rev1)
from keyboards.minivan_rev3 import keyboard as minivan_rev3
KEYBOARDS.append(minivan_rev3)
from keyboards.roadkit import keyboard as roadkit
KEYBOARDS.append(roadkit)
from keyboards.transitvan import keyboard as transitvan
KEYBOARDS.append(transitvan)
from keyboards.provan import keyboard as provan
KEYBOARDS.append(provan)
from keyboards.minorca import keyboard as minorca
KEYBOARDS.append(minorca)
from keyboards.ergodox import keyboard as ergodox
KEYBOARDS.append(ergodox)
from keyboards.caravan import keyboard as caravan
KEYBOARDS.append(caravan)
from keyboards.lowwriter import keyboard as lowwriter
KEYBOARDS.append(lowwriter)

app = Flask(__name__)

# Returns the file to download at the very end
@app.route('/downloads/<firmware>/<filename>')
def download_file(filename, firmware):
    return send_from_directory("/app/tmk_keyboard/keyboard/{0}".format(firmware),
                               filename)


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
        keyboard_name = request.form.get('keyboard', '')
        keyboard = None
        for k in KEYBOARDS:
            if k.name == keyboard_name:
                keyboard = k
                break

        if keyboard is None:
            return('error: no keyboard specified')

        activeLayout = int(request.form.get('activeLayout', '0'))
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
        layer8 = request.form.getlist('L8')
        layer8types = request.form.getlist('LT8')
        layer8mods = request.form.getlist('LM8')
        layer9 = request.form.getlist('L9')
        layer9types = request.form.getlist('LT9')
        layer9mods = request.form.getlist('LM9')
        layer10 = request.form.getlist('L10')
        layer10types = request.form.getlist('LT10')
        layer10mods = request.form.getlist('LM10')
        layer11 = request.form.getlist('L11')
        layer11types = request.form.getlist('LT11')
        layer11mods = request.form.getlist('LM11')
        layer12 = request.form.getlist('L12')
        layer12types = request.form.getlist('LT12')
        layer12mods = request.form.getlist('LM12')
        layer13 = request.form.getlist('L13')
        layer13types = request.form.getlist('LT13')
        layer13mods = request.form.getlist('LM13')
        layer14 = request.form.getlist('L14')
        layer14types = request.form.getlist('LT14')
        layer14mods = request.form.getlist('LM14')
        layer15 = request.form.getlist('L15')
        layer15types = request.form.getlist('LT15')
        layer15mods = request.form.getlist('LM15')

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

        if layer8:
            layers.append({'values': layer8, 'types': layer8types, 'mods': layer8mods})

        if layer9:
            layers.append({'values': layer9, 'types': layer9types, 'mods': layer9mods})

        if layer10:
            layers.append({'values': layer10, 'types': layer10types, 'mods': layer10mods})

        if layer11:
            layers.append({'values': layer11, 'types': layer11types, 'mods': layer11mods})

        if layer12:
            layers.append({'values': layer12, 'types': layer12types, 'mods': layer12mods})

        if layer13:
            layers.append({'values': layer13, 'types': layer13types, 'mods': layer13mods})

        if layer14:
            layers.append({'values': layer14, 'types': layer14types, 'mods': layer14mods})

        if layer15:
            layers.append({'values': layer15, 'types': layer15types, 'mods': layer15mods})

        keys_per_layer = keyboard.layouts[activeLayout]['num_keys']
        template = keyboard.layouts[activeLayout]['layout']

        for layer in layers:
            if (len(layer['values']) != keys_per_layer):
                return('error: some values are missing! please enter all information!')

        layers, fn_actions = kbd.buildFnActions(layers)

        for layer in layers:
            layer = kbd.makeUpper(layer)
            layer = kbd.translateList(layer)
            if not(kbd.isAllowed(layer)):
                return('error: there are invalid characters. please check your imput!<p>{0}</p>'.format(layer))

        keymaps = kbd.buildKeyMaps(layers, template)

        #We can now insert all the values we got into the template file we use. This point can 'propably' be improved still...
        configfile = kbd.createTemplate(fn_actions, keymaps)

        #As soon as we have the entire content of our config, we can write it into a file (with the timestamp we made right at the start!)
        filename = "keymap_{0}_{1}.c".format(keyboard.firmware_folder, now)
        callname = "{0}_{1}".format(keyboard.firmware_folder, now)
        with open("/app/tmk_keyboard/keyboard/{0}/{1}".format(keyboard.firmware_folder, filename), "w+") as templatefile:
            templatefile.write(configfile)
            templatefile.close()

        #everything is set up, now we just have to make our hex file with a system call
        callstring = "make KEYMAP="+callname+" TARGETFILE="+callname+" > /dev/null"
        subprocess.call(callstring, shell=True, cwd="/app/tmk_keyboard/keyboard/{0}/".format(keyboard.firmware_folder))

        #everything is done, we have to return the hex file! :)
        return redirect(url_for('download_file', filename=callname+'.hex', firmware=keyboard.firmware_folder))

    #this is what happens on a GET request, we just send the index.htm file.
    else:
        return send_from_directory("/app/frontend/", "index.html")
