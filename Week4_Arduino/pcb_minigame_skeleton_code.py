# PCB Arduino Mini Game
# Created By : [Your Name]
# Created Date : [Date]
# Version : 1.0

from time import sleep, time
from pymata4 import pymata4
from random import randrange


# ── Pin Configuration ─────────────────────────────────────────────────────────
inputPins  = [3, 4, 5, 6, 7]    # push buttons
outputPins = [8, 9, 10, 11, 12]  # LEDs

# ── Game Settings ─────────────────────────────────────────────────────────────
MAX_LEVEL    = 15   # level at which the game is won
TIMEOUT_TIME = 25   # seconds the player has per input phase

# ── Board Setup ───────────────────────────────────────────────────────────────
board = pymata4.Pymata4()

userSeq = []  # populated by button_callback, read in main


def button_callback(data):
    """
    Callback triggered by pymata4 whenever a digital input pin changes state.
    Appends the pressed pin number to userSeq.

    Parameters:
        data (list): [pin_type, pin_number, value, timestamp] supplied by pymata4
    Returns:
        None
    """
    pinValue  = data[2]
    pinNumber = data[1]
    if pinValue:  # 1 = pressed, 0 = released
        userSeq.append(pinNumber)
        sleep(0.1)  # debounce delay to avoid multiple counts for a single press


for pin in inputPins:
    board.set_pin_mode_digital_input(pin, callback=button_callback)

for pin in outputPins:
    board.set_pin_mode_digital_output(pin)


# ─────────────────────────────────────────────────────────────────────────────
def generate_sequence(level):
    """
    Builds a random LED sequence and the matching expected button sequence.
    Sequence length grows with the level.

    Parameters:
        level (int): the current game level
    Returns:
        lightSeq    (list): output pins to flash in order
        expectedSeq (list): corresponding input pins the player must press
    """
    lightSeq    = []
    expectedSeq = []

    for i in range(level + 3):
        randomIndex = randrange(0, len(outputPins))
        lightSeq.append(outputPins[randomIndex])
        expectedSeq.append(inputPins[randomIndex])  # same index = matching button

    return lightSeq, expectedSeq


# ─────────────────────────────────────────────────────────────────────────────
def display_sequence(lightSeq):
    """
    Flashes each LED in the sequence so the player can memorise the order.

    Parameters:
        lightSeq (list): output pin numbers to flash in order
    Returns:
        None
    """
    for light in lightSeq:
        board.digital_write(light, 1)
        sleep(0.5)
        board.digital_write(light, 0)
        sleep(0.5)


# ─────────────────────────────────────────────────────────────────────────────
def main():
    """
    Entry point and main game loop. Runs Simon Says from level 1 up to MAX_LEVEL.
    Handles sequence generation, display, user input validation, and timeout.

    Parameters:
        None
    Returns:
        None
    """
    global userSeq

    level = 1
    lost  = False

    print("The game is starting!!!")

    try:
        # TODO: implement the main game loop here, including sequence generation, display, user input validation, and timeout handling.

        
    except KeyboardInterrupt:
        print("User quit — the game has ended!")

    print(f"Level reached: {level}")

if __name__ == "__main__":
    main()
    board.shutdown()