from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

while keyboard.is_pressed('q') != True:
    if pyautogui.locateOnScreen("his and civ.png")!= None:
        pyautogui.click('his and civ.png')
    if pyautogui.locateOnScreen("Join.png")!= None:
        pyautogui.click('Join.png')
    if pyautogui.locateOnScreen("Join2.png")!= None:
        pyautogui.click('Join2.png')
    if pyautogui.locateOnScreen("Full_screen.png")!= None:
        pyautogui.click('Full_screen.png')
    if pyautogui.locateOnScreen('leave.png')!= None:
        time.sleep(3600)
        pyautogui.click('leave.png')
        
        
   
