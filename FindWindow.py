from numpy import e
from pyautogui import * 
from win32gui import * 
import pyautogui 
import time 
import keyboard
import cv2
import re

imgCast = cv2.imread(r"C:\\Users\\HarrE\\Desktop\\Python Projects\\GitHub\\New World Fishing\\Cast.png")
imgLure = cv2.imread(r"C:\\Users\\HarrE\\Desktop\\Python Projects\\GitHub\\New World Fishing\\Lure.png")
imgHook = cv2.imread(r"C:\\Users\\HarrE\\Desktop\\Python Projects\\GitHub\\New World Fishing\\Hook.png")
imgReel = cv2.imread(r"C:\\Users\\HarrE\\Desktop\\Python Projects\\GitHub\\New World Fishing\\Reel.png") # Colour 1bffd9
imgRelease = cv2.imread(r"C:\\Users\\HarrE\\Desktop\\Python Projects\\GitHub\\New World Fishing\\Release.png")

def winRectLoc(progName):
    window_handle = FindWindow(None, progName)
    if GetWindowRect(window_handle):
        windowLocation = GetWindowRect(window_handle)
        x,y,x1,y1 = windowLocation
        x += 8
        y += 8
        x1 -= x+8
        y1 -= y+8
        print(windowLocation, "--", x,y,x1,y1)
        return x,y,x1,y1
    else:
        raise NameError()

x,y,x1,y1 = winRectLoc("New World")

def timeOut():
    print("------------- Timeout starts in 3 seconds -------------")
    time.sleep(3)
    pyautogui.keyDown('w')
    time.sleep(0.3)
    pyautogui.keyUp('w')
    time.sleep(0.5)
    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')
    time.sleep(1)
    for i in range(3):
        print("------------- Time out finishes in ",3-i," seconds -------------")
        time.sleep(1)

def fishing():
    startTime = time.time()
    endTime = startTime + 300
    while endTime > startTime:
        startTime = time.time()
        # while keyboard.is_pressed('space') == False:
        CastLocation = pyautogui.locateOnScreen(imgCast, region=(x,y,x1,y1), grayscale=True, confidence=0.9) #8
        # LureLocation = pyautogui.locateOnScreen(imgLure, region=(x,y,x1,y1), grayscale=False, confidence=0.7) #5
        HookLocation = pyautogui.locateOnScreen(imgHook, region=(x,y,x1,y1), grayscale=True, confidence=0.6) #6
        ReelLocation = pyautogui.locateOnScreen(imgReel, region=(x,y,x1,y1), grayscale=False, confidence=0.7) #5
        ReleaseLocation = pyautogui.locateOnScreen(imgRelease, region=(x,y,x1,y1), grayscale=True , confidence=0.6) #6/7
        # TimeOutPrompt = pyautogui.locateOnScreen(imgRelease, region=(x,y,x1,y1), grayscale=True , confidence=0.6)
        if CastLocation != None:
            print("Casting",CastLocation,sep="\n")
            pyautogui.click(None,None)
            time.sleep(0.1)
        elif HookLocation != None:
            print("Fish on!", HookLocation,sep="\n")
            pyautogui.mouseDown(x=None, y=None, button='left')
            time.sleep(0.1)
        elif ReelLocation != None:
            print("Reeling it in",ReelLocation,sep="\n")
            pyautogui.mouseDown(x=None, y=None, button='left')
        elif ReleaseLocation != None:
            print("Release",ReleaseLocation,sep="\n")
            pyautogui.mouseUp(x=None, y=None, button='left')
            time.sleep(1)
        elif keyboard.is_pressed('space') == True:
            pyautogui.mouseUp(x=None, y=None, button='left')
            return None
        else:
            # print("No fish")
            pyautogui.mouseUp(x=None, y=None, button='left')
            time.sleep(0.1)

    pyautogui.keyDown('f3')
    time.sleep(0.3)
    pyautogui.keyUp('f3')
    timeOut()

while keyboard.is_pressed('space') == False:
    for i in range(5):
        print("------------- Your have ",5-i," seconds to press space -------------")
        time.sleep(1)
    print("------------- Fishing -------------")
    pyautogui.keyDown('f3')
    time.sleep(0.3)
    pyautogui.keyUp('f3')
    fishing()

print("------------- Script Finished -------------")