#Pull down the menu from the top. 
import pyautogui
import time

title = 'MAR-LX1A'
phone = pyautogui.getWindowsWithTitle(title)[0]

xMidNumber = (phone.width)/2
bottom = phone.bottom
top = phone.top

pyautogui.moveTo(phone.left + xMidNumber, bottom - 225)
time.sleep(.5)
pyautogui.dragTo(phone.left + xMidNumber, top + 160, duration=1)