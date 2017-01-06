# coding: utf8
from common import Keyboard

layouts = []
STANDARD_LAYOUT =  'KEYMAP({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12},' # 13
STANDARD_LAYOUT += '{14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26},' # 13
STANDARD_LAYOUT += '{27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39},' # 13
STANDARD_LAYOUT += '{40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52},' # 13
STANDARD_LAYOUT += '{53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {13}),' # 10
layouts.append({'layout':STANDARD_LAYOUT, 'num_keys':62})

keyboard = Keyboard(
        name='provan',
        description='ProVan 60 PCB',
        firmware_folder='provan',
        layouts=layouts
)