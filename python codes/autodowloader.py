import pyautogui
import time


pyautogui.moveTo(100, 100, duration=1)

# Click the mouse at the specified location
pyautogui.click(100, 100)

# Simulate holding down the "Shift" key
pyautogui.keyDown('shift')




# Release the "Shift" key
pyautogui.keyUp('shift')

# Optional: Add a delay to observe the actions
time.sleep(2)

# Move the mouse back to the original position
pyautogui.moveTo(200, 200, duration=1)

# Click again
pyautogui.click(200, 200)

# You can customize this script by adjusting the coordinates and adding more actions as needed.