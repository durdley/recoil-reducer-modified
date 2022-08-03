import time
import win32api
import random
import keyboard

## Configuration
# Set the MAX horizontal limit. For example, hr=10 means that the program will adjust the position horizontally by 10 px AT MOST.
horizontal_range = 2
# Set the MIN and MAX vertical limit. See above comment(line 10)
min_vert = 5
max_vert = 11
# MIN and MAX delay(in seconds) between shots. (Should be as close to the weapon's fire rate as possible)
min_firerate = 0.04
max_firerate = 0.06
# Toggle keybind
toggle_button = '0'
# Enabled by default?
enabled = False

def is_mouse_down():    # Returns true if the left mouse button is being pressed
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

# Some prints for startup
print("Anti-recoil script initiated.")
if enabled:
    print("STATUS: ENABLED")
else:
    print("STATUS: DISABLED")

last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    # If the toggle button is pressed, toggle the on/off state and print status
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("ANTI-RECOIL ACTIVATED")
            else:
                print("ANTI-RECOIL DEACTIVATED")
    
    if is_mouse_down() and enabled:
        # Between every shot an offset is generated for the next cursor adjustment
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const, 1) / offset_const
        vertical_offset = random.randrange(min_vert * offset_const, max_vert * offset_const, 1) / offset_const

        # Mouse Offset
        win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))

        # Random time offset
        time_offset = random.randrange(min_firerate * offset_const, max_firerate * offset_const, 1) / offset_const
        time.sleep(time_offset)
    # Delay for the loop
    time.sleep(0.001)



