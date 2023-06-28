from pyautogui import *
from PIL import Image
from PIL import ImageGrab
import matplotlib.pyplot as plt 
import PIL.ImageOps
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import pytesseract
import pygetwindow
import cv2


#Functions

def click(x,y):
    wi32.api.SetCursorPos((x,y))
    win32.api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


#Stuff


time.sleep(.5)

#Check if recruitment timer is on screen
recruitmentTimerLocation = pyautogui.locateOnScreen('recruitment-timer.png', grayscale=True, confidence=0.7)
if recruitmentTimerLocation != None:
    print(recruitmentTimerLocation)
    screenshot = ImageGrab.grab(bbox=(recruitmentTimerLocation.left, recruitmentTimerLocation.top, recruitmentTimerLocation.left + recruitmentTimerLocation.width, recruitmentTimerLocation.top + recruitmentTimerLocation.height))
    actuallyScreenshot = ImageGrab.grab(bbox=(recruitmentTimerLocation.left, recruitmentTimerLocation.top + recruitmentTimerLocation.height, recruitmentTimerLocation.left + recruitmentTimerLocation.width, recruitmentTimerLocation.top + (recruitmentTimerLocation.height * 2)))
    actuallyScreenshot.save('ss.png')
else:
    print('No recruitment timer found on screen')
    sys.exit()

#Read text from image
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kis15\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#print(pytesseract.image_to_string(r'ss.png'))
#print(pytesseract.image_to_string(r'ranged.png'))


#Find boxes?
img = cv2.imread('ss.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,50,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

for cnt in contours:
    x1,y1 = cnt[0][0]
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        ratio = float(w)/h
        if ratio != 1 and ratio > 3:
            img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
            #print (cnt)
        

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(pytesseract.image_to_boxes(r'ss.png'))
