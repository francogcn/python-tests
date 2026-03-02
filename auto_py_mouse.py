#This script moves the mouse Randomly On Screen within a determined area
#pip install pyautogui
#Import Required modules
import pyautogui
import time
import random 
# Get screen size to define boundaries for random movement
#screen_width, screen_height = pyautogui.size()
try:
    while True:
        # Generate random coordinates within screen boundaries
        x = random.randint(50, 1200)
        y = random.randint(200, 800)

        # Move to the random coordinates with a short duration
        pyautogui.moveTo(x, y, duration=0.25)
        pyautogui.click(x,y)
        pyautogui.vscroll(-10)
        # Wait for 15 seconds before the next move
        time.sleep(15)
except pyautogui.FailSafeException:
    print("Script terminated by user (mouse moved to corner).")
except KeyboardInterrupt:

    print("Script terminated by user (Ctrl+C).")
