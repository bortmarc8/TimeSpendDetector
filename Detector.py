from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os

#Getting all images from the Programs folder
FOLDER_PATH = os.getcwd() + "\Programs"
fileNames = os.listdir(FOLDER_PATH)

#Main code
while 1: 
    f = open("OutputFile.txt")

    for filePath in fileNames:
        print("Iteration")
        fileName = filePath.rsplit("Programs\\")
        if pyautogui.locateOnScreen("Programs\\" + fileName[0]) == None:
            f.write("Programs\\" + fileName[0])
            f.close()
            time.sleep(0.9)
