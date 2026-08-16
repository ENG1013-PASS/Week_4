# Pedestrian Crossing Simulation
# Created By : [Your Name]
# Created Date : [Date]
# Version : 1.0
# Description : Simulates a pedestrian crossing using digital input/output pins.
#               Pressing the pedestrian button triggers a traffic light sequence
#               that allows pedestrians to cross before resuming normal operation.

from pymata4 import pymata4
from time import sleep


# ── Pin Configuration ─────────────────────────────────────────────────────────
inputPins  = [3, 4, 5, 6, 7]    # buttons  (RED, GREEN, BLUE, YELLOW, WHITE)
outputPins = [8, 9, 10, 11, 12]  # LEDs     (RED, GREEN, BLUE, YELLOW, WHITE)

# Named pins for clarity
redLight        = 8
greenLight      = 9
yellowLight     = 11
pedestrianLight = 12   # WHITE
pedestrianBtn   = 5    # D5

# ── Timings ───────────────────────────────────────────────────────────────────
YELLOW_DURATION = 2     # seconds traffic light stays yellow
WALK_DURATION   = 3     # seconds pedestrian light stays solid
FLASH_DURATION  = 2     # seconds pedestrian light flashes
FLASH_SPEED     = 0.25  # seconds per on/off flash cycle

# ── Board Setup ───────────────────────────────────────────────────────────────
board = pymata4.Pymata4()

crossingRequested = False


def button_callback(data):
    """
    Callback triggered when any input pin changes state.
    Sets crossingRequested to True when the pedestrian button D5 is pressed.

    Parameters:
        data (list): [pin_type, pin_number, value, timestamp] from pymata4
    Returns:
        None
    """
    global crossingRequested
    pinNumber = data[1]
    value     = data[2]

    if pinNumber == pedestrianBtn and value == 1:
        pass
        #TODO: Implement logic to handle pedestrian button press


for pin in inputPins:
    board.set_pin_mode_digital_input(pin, callback=button_callback)

for pin in outputPins:
    board.set_pin_mode_digital_output(pin)


# ─────────────────────────────────────────────────────────────────────────────
def main():
    """
    Main loop. Starts in normal operation with the green traffic light on.
    Monitors for a crossing request and runs the crossing sequence when triggered.

    Parameters:
        None
    Returns:
        None
    """
    global crossingRequested

    board.digital_write(greenLight, 1)
    print("System ready. Waiting for pedestrian request...")

    try:
        #TODO: Implement the main loop logic to handle traffic light sequencing and pedestrian crossing requests.
        pass

    except KeyboardInterrupt:
        print("Shutting down...")
        for pin in outputPins:
            board.digital_write(pin, 0)
        board.shutdown()


if __name__ == "__main__":
    main()
