import pyautogui
import time
from random import randint

def startGame():
    pyautogui.click(1557, 291, button = 'left')
    pyautogui.click(928, 723, button = 'left')
    time.sleep(.1)
    print('Game Started')
    chooseSkin()

def chooseSkin():
    y = 845
    number = randint(0, 8)
    x = 630 + number * 80
    print(number)
    pyautogui.click(x, y, button = 'left')
    time.sleep(.1)
    print('Skin Chosen')
    chooseEyes()

def chooseEyes():
    pyautogui.click(695, 750, button = 'left')
    #-----------------
    eyelashNumber = randint(0,1)
    eyelashes = 909 + eyelashNumber * 80
    pyautogui.click(eyelashes, 849, button = 'left')
    time.sleep(.1)
    #-----------------
    colorNumber = randint(0, 7)
    print(colorNumber)
    x = 670 + colorNumber * 80
    pyautogui.click(x, 923, button = 'left')
    time.sleep(.1)
    print('Eyes Chosen')
    chooseMouth()

def chooseMouth():
    pyautogui.click(755, 750, button = 'left')
    #------------------
    colorNumber = randint(0, 2)
    print(colorNumber)
    x = 870 + colorNumber * 80
    pyautogui.click(x, 847, button = 'left')
    time.sleep(.1)
    print('Mouth Chosen')
    chooseEyebrows()

def chooseEyebrows():
    pyautogui.click(861, 750, button = 'left')
    #------------------
    thicknessNumber = randint(0,1)
    print(thicknessNumber)
    x = 913 + thicknessNumber*80
    pyautogui.click(x, 847, button = 'left')
    time.sleep(.1)
    #------------------
    colorNumber = randint(0, 12)
    if colorNumber > 9:
        pyautogui.click(1383, 919, button = 'left')
        colorClicked = 587 + (colorNumber - 3)*80
        pyautogui.click(colorClicked, 925, button = 'left')
    else:
        colorClicked = 587 + (colorNumber)*80
        pyautogui.click(colorClicked, 925, button = 'left')
    print('Eyebrows Chosen')
    
    


def main():
    pass
    
