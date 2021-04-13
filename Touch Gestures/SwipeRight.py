#Pull down the menu from the top. 
import pyautogui
import time

title = 'MAR-LX1A'
phone = pyautogui.getWindowsWithTitle(title)[0]

xCordLeft = (phone.left) + 20
yCordmid = (phone.height)/2

pyautogui.moveTo(phone.right - 20, phone.top + yCordmid)
time.sleep(.5)
pyautogui.dragTo(xCordLeft, yCordmid, duration=.8)