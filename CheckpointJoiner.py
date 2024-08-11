from PIL import ImageGrab
import numpy as np
import pyautogui
import keyboard
import multiprocessing
from time import sleep

chat_coords = (2214, 1136, 2474, 1156)
inv_coords = [1955, 1255]
checkpoint_account = 'joe'  # bungie name of checkpoint account
green_threshold = 115
exit_key = 'p'
test_mode = False


if test_mode:
    while True:
        print(pyautogui.position())
        print(ImageGrab.grab().getpixel(inv_coords)[1])
        sleep(0.5)


def main_loop():
    hasJoinedFromOrbit = False
    sleep(3)
    print('waiting')
    while True:
        if ImageGrab.grab().getpixel(inv_coords)[1] > green_threshold:
            print('joining')
            keyboard.send('enter')
            sleep(0.5)
            keyboard.write(f'/join {checkpoint_account}', 0.1)
            keyboard.send('enter')
            sleep(1)
            if hasJoinedFromOrbit:
                keyboard.send('enter')
                sleep(3)
            else:
                hasJoinedFromOrbit = True
            print('joined')
            sleep(20)
            print('waiting')
        sleep(1)


def main():
    exit_process = multiprocessing.Process(target=keyboard.wait, args=exit_key)
    main_process = multiprocessing.Process(target=main_loop)
    exit_process.start()
    main_process.start()
    exit_process.join()
    main_process.terminate()


if __name__ == '__main__':
    main()
