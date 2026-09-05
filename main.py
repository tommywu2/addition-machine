digit = {
    "ZERO" : "0",
    "ONE" : "1",
}

symbol = {
    "OUTPUT" : "‖",
    "LEFT_START" : "⊢",
    "RIGHT_START" : "⊣",
    "BLANK" : "·",
    "ONE" : "X",
    "ZERO" : "O",
}

operator = {
    "PLUS" : "+",
}

move = {
    "LEFT" : "→",
    "RIGHT" : "←",
    "HALT" : "⏹",
}

state = {
    "START", "SETUP", "REWIND", "SETUP_2", "SETUP_2_ZERO", "SETUP_2_ONE", "FIND", "TO_COUNT", "INCREMENT", "RESTORE", "OUTPUT_RESET"
}

machine = {}

def add(curr_state, curr_symbol, next_symbol, next_state, move):
    machine.append(curr_state, curr_symbol, next_symbol, next_state, move)

def __init__():
    add(state.START, symbol.LEFT_WALL, None, state.SETUP, move.RIGHT)
    add(state.SETUP, symbol.RIGHT_WALL, symbol.OUTPUT, None, move.RIGHT)
    add(state.SETUP, symbol.BLANK, symbol.RIGHT_WALL, state.SETUP_REWIND, move.LEFT)
    add(state.SETUP_REWIND, symbol.LEFT_WALL, None, state.SETUP_2, move.RIGHT)
    add(state.SETUP_2, digit.ONE, symbol.ONE, state.SETUP_2_ONE, move.RIGHT)
    add(state.SETUP_2, digit.ZERO, symbol.ZERO, state.SETUP_2_ZERO, move.RIGHT)
    add(state.SETUP_2_ONE, symbol.RIGHT_WALL, digit.ONE, None, move.RIGHT)
    add(state.SETUP_2_ZERO, symbol.RIGHT_WALL, digit.ZERO, None, move.RIGHT)
    add(state.SETUP_2_ONE, symbol.BLANK, symbol.RIGHT_WALL, state.SETUP_REWIND, move.LEFT)
    add(state.SETUP_2_ZERO, symbol.BLANK, symbol.RIGHT_WALL, state.SETUP_REWIND, move.LEFT)
    add(state.SETUP_2, operator.PLUS, None, state.FIND, move.RIGHT)
    add(state.FIND, digit.ONE, symbol.ONE, state.TO_COUNT, move.RIGHT)
    add(state.FIND, digit.ZERO, symbol.ZERO, None, move.RIGHT)
    add(state.TO_COUNT, symbol.OUTPUT, None, state.INCREMENT, move.RIGHT)
    add(state.INCREMENT, digit.ZERO, digit.ONE, state.SETUP_REWIND, move.LEFT)
    add(state.SETUP_REWIND, symbol.PLUS, None, state.FIND, move.RIGHT)
    add(state.INCREMENT, digit.ONE, digit.ZERO, None, move.RIGHT)
    add(state.INCREMENT, symbol.RIGHT_WALL, None, state.OUTPUT_RESET, move.LEFT)
    add(state.OUTPUT_RESET, digit, digit.ZERO, None, move.LEFT)
    add(state.OUTPUT_RESET, symbol.OUTPUT, None, state.SETUP_REWIND, move.LEFT)
    add(state.FIND, symbol.OUTPUT, None, state.RESTORE, move.RIGHT)
    add(state.RESTORE, symbol.ONE, digit.ONE, None, move.LEFT)
    add(state.RESTORE, symbol.ZERO, digit.ZERO, None, move.LEFT)
    add(state.RESTORE, symbol.LEFT_WALL, None, state.DONE, move.HALT)