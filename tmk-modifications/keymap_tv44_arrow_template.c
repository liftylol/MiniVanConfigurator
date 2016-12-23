#include "keymap_common.h"

const uint8_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /* 0: qwerty */
    KEYMAP(replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace),

    /* 1: FN 1 */
     KEYMAP(replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
			replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
			replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
			replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace),

    /* 2: FN 2 */
    KEYMAP(replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace),

    /* 3:  Game Mode */
    KEYMAP(replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace, \
           replace,  replace,   replace,   replace,   replace,   replace,   replace,   replace,   replace),

   /* 4:  LED Mode */
   KEYMAP(TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS, TRNS, \
          TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,  TRNS,  TRNS,  TRNS,  TRNS,  TRNS, \
          TRNS,    TRNS,   TRNS,   TRNS,   TRNS,   TRNS,   TRNS,  TRNS, TRNS, TRNS, TRNS,TRNS, \
          TRNS, TRNS,     TRNS,  TRNS,       TRNS,      TRNS, TRNS, TRNS, TRNS),
};

const uint16_t PROGMEM fn_actions[] = {
    [0]  = ACTION_LAYER_MOMENTARY(1),
    [1]  = ACTION_LAYER_MOMENTARY(2),
    [2]  = ACTION_LAYER_TOGGLE(3),
    [3]  = ACTION_MODS_KEY(MOD_LSFT, KC_GRV),
    [4]  = ACTION_MODS_KEY(MOD_LSFT, KC_1),
    [5]  = ACTION_MODS_KEY(MOD_LSFT, KC_2),
    [6]  = ACTION_MODS_KEY(MOD_LSFT, KC_3),
    [7]  = ACTION_MODS_KEY(MOD_LSFT, KC_4),
    [8]  = ACTION_MODS_KEY(MOD_LSFT, KC_5),
    [9]  = ACTION_MODS_KEY(MOD_LSFT, KC_6),
    [10] = ACTION_MODS_KEY(MOD_LSFT, KC_7),
    [11] = ACTION_MODS_KEY(MOD_LSFT, KC_8),
    [12] = ACTION_MODS_KEY(MOD_LSFT, KC_9),
    [13] = ACTION_MODS_KEY(MOD_LSFT, KC_0),
    [14] = ACTION_MODS_KEY(MOD_LSFT, KC_BSLS),
    [15] = ACTION_MODS_KEY(MOD_LSFT, KC_QUOT),
    [16] = ACTION_MODS_KEY(MOD_LSFT, KC_MINS),
    [17] = ACTION_MODS_KEY(MOD_LSFT, KC_EQL),
    [18] = ACTION_MODS_KEY(MOD_LSFT, KC_LBRC),
    [19] = ACTION_MODS_KEY(MOD_LSFT, KC_RBRC),
    [20] = ACTION_LAYER_TOGGLE(4),
};
