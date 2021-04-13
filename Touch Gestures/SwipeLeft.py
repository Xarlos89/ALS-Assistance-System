#Pull down the menu from the top. 
import pyautogui
import time

title = 'MAR-LX1A'
phone = pyautogui.getWindowsWithTitle(title)[0]

xCordright = (phone.width)-30
yCordmid = (phone.height)/2

pyautogui.moveTo(phone.left + 10, phone.top + yCordmid)
time.sleep(.5)
pyautogui.drag(xCordright, 0, duration=1)

