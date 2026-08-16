# Task: Pedestrian Crossing Simulation

In this task you will simulate a basic pedestrian crossing using the PCB. This is very similar to a feature you will need to implement in the actual project, so it's good practice.

---

## Pin Reference

The PCB lights and buttons are mapped as follows (left to right):

| Colour | Output Pin | Input Pin |
|--------|------------|-----------|
| RED    | D8         | D3        |
| GREEN  | D9         | D4        |
| BLUE   | D10        | D5        |
| YELLOW | D11        | D6        |
| WHITE  | D12        | D7        |

For this task:
- **GREEN (D9)** = traffic light green
- **RED (D8)** = traffic light red
- **YELLOW (D11)** = traffic light yellow
- **WHITE (D12)** = pedestrian light (on = green / walk, off = red / don't walk)
- **D5** = pedestrian push button

> **Note:** We are not using a dedicated pedestrian "red" LED here. The pedestrian light is simply WHITE on (walk) or WHITE off (don't walk). This is because on this PCB, each LED and its corresponding button share a connection, so having a light on while trying to read its button causes interference. Keeping unused lights off avoids this.

---

## Normal Operation

When the system starts, it should be in its default state:

- **GREEN on** = traffic is flowing
- All other lights off

---

## When D5 is Pressed

Pressing the pedestrian button (D6) should trigger the following sequence:

1. Traffic light goes **YELLOW** for 2 seconds
2. Traffic light goes **RED** (yellow turns off)
3. **WHITE turns on** = pedestrian may cross (3 seconds)
4. **WHITE flashes** = pedestrian crossing ending (2 seconds)
5. WHITE turns off, **GREEN turns back on** = traffic resumes

---

## Your Task

Using what you know about callbacks and digital input/output pins:

1. Set up all input and output pins using a loop (as you have done before)
2. Use a **callback function** on D5 to detect when the button is pressed
3. Implement the crossing sequence in `main`

Think about: what should happen if the button is pressed *while the sequence is already running*? For now, it's fine to ignore it — but keep it in mind.

---

## Skeleton Code

Skeleton code is provided in `pedestrian_crossing.py` to get you started.
