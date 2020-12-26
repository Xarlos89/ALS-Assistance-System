# Script pulls from left to right
import pyautogui

pyautogui.moveTo(1470, 500)
pyautogui.dragTo(1830, 500, .5, pyautogui.easeInQuad, button='left')
