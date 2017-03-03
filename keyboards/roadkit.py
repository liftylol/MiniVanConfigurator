# coding: utf8
from common import Keyboard

layouts = []
STANDARD_LAYOUT =  'KEYMAP({},  {},   {},   {},'
STANDARD_LAYOUT += '{},  {},   {},'
STANDARD_LAYOUT += '{},  {},   {},   {},'
STANDARD_LAYOUT += '{},  {}),'
layouts.append({'layout':STANDARD_LAYOUT, 'num_keys':13})

SINGLES_LAYOUT =  'SINGLES_KEYMAP({},  {},   {},   {},'
SINGLES_LAYOUT += '{},  {},   {},   {},'
SINGLES_LAYOUT += '{},  {},   {},   {},'
SINGLES_LAYOUT += '{},  {},   {},   {}),'
layouts.append({'layout':SINGLES_LAYOUT, 'num_keys':16})

keyboard = Keyboard(
        name='roadkit',
        description='Roadkit Round 1 PCBs',
        firmware_folder='roadkit',
        layouts=layouts
)