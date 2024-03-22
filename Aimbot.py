import pyautogui
import cv2
import numpy as np
import time

target_image = cv2.imread('target.png')

while True:
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    screenshot = np.array(screenshot)
    screenshot_rgb = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

    # Find target
    result = cv2.matchTemplate(screenshot_rgb, target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    target_x, target_y = max_loc[0] + target_image.shape[1] // 2, max_loc[1] + target_image.shape[0] // 2

    # Get the current position of the mouse
    mouse_x, mouse_y = pyautogui.position()

    # Move the mouse towards the target
    if mouse_x < target_x:
        pyautogui.move(-1, 0)
    elif mouse_x > target_x:
        pyautogui.move(1, 0)

    if mouse_y < target_y:
        pyautogui.move(0, 1)
    elif mouse_y > target_y:
        pyautogui.move(0, -1)

    # Delay to avoid detection
    time.sleep(0.01)