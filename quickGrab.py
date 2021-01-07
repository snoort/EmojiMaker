from PIL import ImageGrab
import os
import time

def screenGrab():
    box = ()
    image = ImageGrab.grab()
    image.save(os.getcwd() + 'picture' + str(int(time.time())) +  '.png', 'PNG')

def main():
    screenGrab()

    if __name__ == '__main__':
        main()
