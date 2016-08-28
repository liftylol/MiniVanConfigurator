# MiniVanConfigurator
This is a website with a python back-end based on flask that allows you to easily configure your MiniVan keyboard online and download the required .hex-file to flash it


The 'front-end' is just a badly writtend html file with a stylesheet that should kind of mimic the original colorscheme of the Midnight Drive keyset that came with the first groupbuy. If anyone with a little more talent wants to improve my front-end i would be very pleased! That's basically the most advanced front-end i ever wrote and that says a lot... Those two files are found in the frontend folder.

The tmk-modifications (shoutouts to hasu and the entire crew for their amazing software!) folder contains two files. The first one is a minimally changed Makefile that just allows me to compile files with a name i want instead of always getting a 'tv44_lufa.hex'. The second one is the template file that my program loads every time and fills in the desired keys. It's just the keymap from evan (shoutouts!) with placeholders for the values to come.

Basically everything interesting is inside van.py. It's a script that is written in Python using the Flask web framework and is delivered by apache with wsig_mod on my server currently. There's a lot of stuff to do still but i just cleaned everything up and made it a lot prettier (could still be better though...). 

I'll list everything below that i want to change/add later on so if anyone is really interested - please go ahead and contact me.

Backend:
- Add support for more/less layers
- Add support for different layer modes (atm the fn1-3 buttons are default, 1-2 are momentary and 3 is toggle. can easily be changed using the template file, everything needed can be set there)

Frontend:
- Prettier website
- Rightclicking onto a key opens a context menu where all special characters can be selected
- Support everything i want to add in my backend
