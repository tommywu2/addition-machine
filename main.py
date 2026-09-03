string = "⊢0000000000000000+0000000000000000⊣"
position = 0

digit = {
    "0" : "0",
    "1" : "1",
}

symbol = {
    "OUTPUT" : "‖",
    "LEFT_START" : "⊢",
    "RIGHT_START" : "⊣",
    "BLANK" : "·"
}
operator = {
    "ADD" : "+",
}

move = {
    "LEFT" : "→",
    "RIGHT" : "←",
}

Tokens = digit | symbol | operator | move

def increment():
    position += 1
    return

def decrement():
    position -= 1
    return

def __init__():
    machine.setup(
        right_to(symbol.RIGHT_START, append(symbol.OUTPUT))
    )

def scan_to(symbol, direction):
    while not string[position] == symbol:
        if direction == move.LEFT:
            increment()
        elif direction == move.RIGHT:
            decrement()
    return string[position]
            
def right_to(symbol, state):
    while not string[position] == symbol:
        increment()
    return string[position]

def append(new_symbol):
    string[position] = new_symbol
    return

def find_and_mark(symbol, mark, end):
    while not string[position] == "⊢":
        decrement()
    while not string[position] == end:
        if string[position] == symbol:
            string[position] == mark
        increment()
    return

def successor():
    while not string[position] == "⊢":
        decrement()
    while not string[position] == "‖":
        increment()
    while not string[position] in "01":
        increment()
    if string[position] in "0":
        string[position] == "1"
    elif string[position] in "1":
        while string[position] == "1":
            string[position] == "0"
            increment()
        if string[position] == "0":
            string[position] == "1"
        elif string[position] == "⊣":
            decrement()
            while not string[position] == "‖":
                string[position] = "0"
                decrement()
    return

def restore_marks(mark, symbol):
    while not string[position] == "⊢":
        decrement()
    while not string[position] == "‖":
        if string[position] == mark:
            string[position] == symbol
        increment()
    return