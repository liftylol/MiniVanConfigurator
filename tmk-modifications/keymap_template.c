#include "keymap_common.h"

const uint8_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
   layers
};

/* id for user defined functions */
enum function_id {
    RESET_KEY,
};

const action_t PROGMEM fn_actions[] = {
    fnactions
};

void action_function(keyrecord_t *event, uint8_t id, uint8_t opt)
{
    if (id == RESET_KEY) {
        clear_keyboard();
        _delay_ms(250);
        bootloader_jump();
    }
}