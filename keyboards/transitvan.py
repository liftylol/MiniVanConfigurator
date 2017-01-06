# coding: utf8
from common import Keyboard

layouts = []
STANDARD_LAYOUT =  'KEYMAP({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},'
STANDARD_LAYOUT += '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},'
STANDARD_LAYOUT += '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},'
STANDARD_LAYOUT += '{}, {}, {}),'
layouts.append({'layout':STANDARD_LAYOUT, 'num_keys':41})

keyboard = Keyboard(
        name='transitvan',
        description='Handwired TransitVan',
        firmware_folder='transitvan',
        layouts=layouts
)