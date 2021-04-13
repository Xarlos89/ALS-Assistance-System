#Pull down the menu from the top. 
import pyautogui
import time

title = 'MAR-LX1A'
phone = pyautogui.getWindowsWithTitle(title)[0]

middle = (phone.width)/2
bottomSide = (phone.bottom) - 250

pyautogui.moveTo(phone.left + middle, phone.top + 37)
time.sleep(.5)
pyautogui.drag(0, bottomSide, duration=1)



