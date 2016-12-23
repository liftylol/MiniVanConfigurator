#include "keymap_common.h"

const uint8_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
   layers

   /* 4:  LED Mode */
   KEYMAP_ARROW(TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS, TRNS, \
          TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,TRNS,  TRNS,  TRNS,  TRNS,  TRNS,  TRNS, \
          TRNS,    TRNS,   TRNS,   TRNS,   TRNS,   TRNS,   TRNS,  TRNS, TRNS, TRNS, TRNS,TRNS, \
          TRNS, TRNS,     TRNS,  TRNS,       TRNS,      TRNS, TRNS, TRNS, TRNS),
};

const uint16_t PROGMEM fn_actions[] = {
    fnactions
};
