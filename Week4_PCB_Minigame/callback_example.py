# Pymata4 Callback Example
# Two buttons, two LEDs, prints callback data on every press
 
from pymata4 import pymata4
from time import sleep
 
board = pymata4.Pymata4()
 
inputPins  = [3, 4]    # buttons
 
 
def button_callback(data):
    pinType   = data[0]  # pin type (2 = digital input)
    pinNumber = data[1]  # which pin was triggered
    value     = data[2]  # 1 = pressed, 0 = released
    timestamp = data[3]
 
    print(f"\n-- Callback fired --")
    print(f"Full data list : {data}")
    print(f"Pin number     : {pinNumber}")
    print(f"Value          : {value}  ({'PRESSED' if value == 1 else 'RELEASED'})")
    print(f"Timestamp      : {timestamp:.2f}")
 
 
for pin in inputPins:
    board.set_pin_mode_digital_input(pin, callback=button_callback)

print("Ready - press either button (Ctrl+C to quit)\n")
 
try:
    while True:
        sleep(1)  # main thread just stays alive; callback does all the work
except KeyboardInterrupt:
    print("\nQuitting...")
    board.shutdown()
 