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

COMMAND_LAYOUT =  'KEYMAP_COMMAND({0},  {1},   {2},   {3},   {4},   {5},   {6},   {7},   {8},   {9},   {10},   {11},'
COMMAND_LAYOUT += '{12},  {13},   {14},   {15},   {16},   {17},   {18},   {19},   {20},   {21},   {22},   {23},'
COMMAND_LAYOUT += '{24},  {25},   {26},   {27},   {28},   {29},   {30},   {31},   {32},   {33},   {34},   {35},'
COMMAND_LAYOUT += '{36},  {37},   {40},   {38},   {39},   {41},   {42},   {43}, {44}),'
layouts.append({'layout':COMMAND_LAYOUT, 'num_keys':45})

ARROW_COMMAND_LAYOUT =  'KEYMAP_ARROW_COMMAND({0},  {1},   {2},   {3},   {4},   {5},   {6},   {7},   {8},   {9},   {10},   {11},'
ARROW_COMMAND_LAYOUT += '{12},  {13},   {14},   {15},   {16},   {17},   {18},   {19},   {20},   {21},   {22},   {23},'
ARROW_COMMAND_LAYOUT += '{24},  {25},   {26},   {27},   {28},   {29},   {30},   {31},   {32},   {33},   {34},   {35},'
ARROW_COMMAND_LAYOUT += '{36},  {37},   {40},   {38},   {39},   {41},   {42},   {43}, {44}, {45}),'
layouts.append({'layout':ARROW_COMMAND_LAYOUT, 'num_keys':46})

keyboard = Keyboard(
        name='low_writer_rev1',
        description='LowWriter Rev 1 PCB',
        firmware_folder='low-writer',
        layouts=layouts
)