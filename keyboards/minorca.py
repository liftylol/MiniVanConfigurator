# coding: utf8
from common import Keyboard

layouts = []
STANDARD_LAYOUT =  'KEYMAP({},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
STANDARD_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
STANDARD_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {},   {},   {},   {},'
STANDARD_LAYOUT += '{},  {},   {},   {},   {},   {},   {},   {}),'
layouts.append({'layout':STANDARD_LAYOUT, 'num_keys':42})

keyboard = Keyboard(
        name='minorca',
        description='Minorca keyboard',
        firmware_folder='minorca',
        layouts=layouts
)