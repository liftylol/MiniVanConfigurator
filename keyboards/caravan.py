# coding: utf8
from common import Keyboard

layouts = []
STANDARD_LAYOUT =  'KEYMAP({},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
STANDARD_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
STANDARD_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
STANDARD_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {}),'
layouts.append({'layout':STANDARD_LAYOUT, 'num_keys':44})

ARROW_LAYOUT =  'KEYMAP_ARROW({},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
ARROW_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
ARROW_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
ARROW_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {}, {}),'
layouts.append({'layout':ARROW_LAYOUT, 'num_keys':45})

keyboard = Keyboard(
        name='caravan',
        description='CaraVan R1 PCBs',
        firmware_folder='caravan',
        layouts=layouts
)