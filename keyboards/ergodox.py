# coding: utf8
from common import Keyboard

layouts = []
STANDARD_LAYOUT =  'KEYMAP({0},{1},{2},{3},{4},{5},{6},'
STANDARD_LAYOUT += '{14},{15},{16},{17},{18},{19},{20},'
STANDARD_LAYOUT += '{28},{29},{30},{31},{32},{33},'
STANDARD_LAYOUT += '{40},{41},{42},{43},{44},{45},{46},'
STANDARD_LAYOUT += '{54},{55},{56},{57},{58},'
STANDARD_LAYOUT += '{64},{65},'
STANDARD_LAYOUT += '{68},'
STANDARD_LAYOUT += '{70},{71},{72},'
STANDARD_LAYOUT += '{7},{8},{9},{10},{11},{12},{13},'
STANDARD_LAYOUT += '{21},{22},{23},{24},{25},{26},{27},'
STANDARD_LAYOUT += '{34},{35},{36},{37},{38},{39},'
STANDARD_LAYOUT += '{47},{48},{49},{50},{51},{52},{53},'
STANDARD_LAYOUT += '{59},{60},{61},{62},{63},'
STANDARD_LAYOUT += '{66},{67},'
STANDARD_LAYOUT += '{69},'
STANDARD_LAYOUT += '{73},{74},{75}),'
layouts.append({'layout':STANDARD_LAYOUT, 'num_keys':76})

keyboard = Keyboard(
        name='ergodox',
        description='Ergodox Teensy PCB',
        firmware_folder='ergodox',
        layouts=layouts
)