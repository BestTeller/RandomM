import os
import random
import time
import pyautogui

# Disable PyAutoGUI's fail-safe feature
pyautogui.FAILSAFE = False

def invert_mouse_movement(x, y):
    """Invert mouse movement: positive becomes negative and vice versa."""
    return -x, -y

def random_mouse_movement(invert=False):
    """Move the mouse cursor randomly, with an option to invert movement."""
    while True:
        x_offset = random.randint(-250, 250)
        y_offset = random.randint(-250, 250)

        if invert:
            x_offset, y_offset = invert_mouse_movement(x_offset, y_offset)

        # Move instantly by setting duration to 0
        pyautogui.moveRel(x_offset, y_offset, duration=0)

if __name__ == "__main__":
    invert = True  # Set to True if you want inverted movement

    # Start the mouse movement
    random_mouse_movement(invert=invert)
