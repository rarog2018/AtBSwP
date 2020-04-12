#! python3
# mouseNudge.py - slightly moves the mouse every 10 seconds

# 1. It should end after the user presses Ctrl+C or triggers FailSafe (moving
# the cursor to the corner)
# 2. It should move the mouse 1 pixel relatively to its current position
# 3. Then, after 10 seconds it should move the mouse 1 pixel to the previous
#    position.

import pyautogui
print('To quit: press Ctrl+C or move the cursor to the corner of the screen')

# try block to catch KeyboardInterrupt exception
try:
    while True:
        pyautogui.moveRel(0, -1)    # move relatively to current position
        pyautogui.PAUSE = 10        # wait 10 seconds
        pyautogui.moveRel(0, 1)

# handle multiple exceptions
except (KeyboardInterrupt, pyautogui.FailSafeException):
    print('Done.')
