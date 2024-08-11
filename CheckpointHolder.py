import pyautogui
import keyboard
import multiprocessing
from time import sleep


join_account = 'ha'  # bungie name of joining account
exit_key = 'p'
test_mode = False


if test_mode:
    while True:
        print(pyautogui.position())
        sleep(0.5)


def release_all():  # this is lazy and stupid. too bad!
    for i in range(ord('a'), ord('z') + 1):
        keyboard.release(chr(i))
    keyboard.release('tab')
    keyboard.release('escape')
    keyboard.release('shift')
    keyboard.release('3')


def main_loop():
    sleep(5)
    while True:
        release_all()
        keyboard.send('m')
        sleep(1.5)
        pyautogui.moveTo(450, 330)
        sleep(0.5)
        pyautogui.click()
        sleep(1.5)
        pyautogui.moveTo(1700, 900)
        sleep(0.5)
        pyautogui.click()
        sleep(4.5)
        pyautogui.moveTo(1700, 500)
        sleep(0.5)
        pyautogui.click()
        sleep(1.5)
        pyautogui.moveTo(1700, 900)
        sleep(0.5)
        pyautogui.click()
        sleep(26)
        #loaded in
        keyboard.press('shift')
        keyboard.press('w')
        sleep(3.7)
        keyboard.send('space')
        sleep(4)
        keyboard.release('w')
        keyboard.release('shift')
        keyboard.release('space')
        keyboard.press('e')
        sleep(2)
        keyboard.release('e')
        keyboard.press('a')
        keyboard.press('w')
        sleep(1)
        keyboard.release('a')
        sleep(0.25)
        keyboard.press('shift')
        sleep(4)
        keyboard.release('shift')
        keyboard.release('w')
        sleep(0.25)
        keyboard.send('3')
        sleep(1)
        keyboard.press('9')  # 9 is bound to fire
        sleep(0.25)
        keyboard.release('9')
        sleep(0.1)
        # send invite to joiner
        keyboard.send('enter')
        sleep(1)
        keyboard.write(f'/invite {join_account}')
        sleep(1)
        keyboard.send('enter')
        sleep(1)
        # set leader and leave
        keyboard.send('m')
        sleep(1)
        keyboard.send('d')
        sleep(1)
        pyautogui.moveTo(1000, 520)
        sleep(0.5)
        pyautogui.click()
        sleep(5)
        pyautogui.moveTo(455, 405)
        sleep(0.5)
        pyautogui.click()
        sleep(0.5)
        keyboard.send('escape')
        sleep(0.75)
        keyboard.press('o')
        sleep(13)


def main():
    exit_process = multiprocessing.Process(target=keyboard.wait, args=exit_key)
    main_process = multiprocessing.Process(target=main_loop)
    exit_process.start()
    main_process.start()
    exit_process.join()
    main_process.terminate()
    release_all()


if __name__ == '__main__':
    main()

