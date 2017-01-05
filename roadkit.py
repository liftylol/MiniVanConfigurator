# coding: utf8
import os, subprocess, datetime, fileinput
from flask import Flask, flash, request, redirect, url_for, send_from_directory
import common as kbd

app = Flask(__name__)

STANDARD_LAYOUT =  'KEYMAP(replace,  replace,   replace,   replace,'
STANDARD_LAYOUT += 'replace,  replace,   replace,'
STANDARD_LAYOUT += 'replace,  replace,   replace,   replace,'
STANDARD_LAYOUT += 'replace,  replace),'

SINGLES_LAYOUT =  'SINGLES_KEYMAP(replace,  replace,   replace,   replace,'
SINGLES_LAYOUT += 'replace,  replace,   replace,   replace,'
SINGLES_LAYOUT += 'replace,  replace,   replace,   replace,'
SINGLES_LAYOUT += 'replace,  replace,   replace,   replace),'

# Returns the file to download at the very end
@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory("/app/tmk_keyboard/keyboard/roadkit",
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
        activeLayout = request.form.get('activeLayout', 0)

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

        keys_per_layer = 13
        template = STANDARD_LAYOUT
        if activeLayout is 1:
            keys_per_layer = 16
            template = SINGLES_LAYOUT

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
        filename = "keymap_roadkit_"+now+".c"
        callname = "roadkit_"+now
        with open("/app/tmk_keyboard/keyboard/roadkit/"+filename, "w+") as templatefile:
            templatefile.write(configfile)
            templatefile.close()

        #everything is set up, now we just have to make our hex file with a system call
        callstring = "make KEYMAP="+callname+" TARGETFILE="+callname+" > /dev/null"
        subprocess.call(callstring, shell=True, cwd="/app/tmk_keyboard/keyboard/roadkit/")

        #everything is done, we have to return the hex file! :)
        return redirect(url_for('download_file', filename=callname+'.hex'))

    #this is what happens on a GET request, we just send the index.htm file.
    else:
        return send_from_directory("/app/frontend/", "index.html")
