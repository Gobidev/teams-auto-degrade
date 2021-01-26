from pyautogui import position, rightClick, moveTo, leftClick
from time import sleep
from keyboard import is_pressed


# position for teams in full screen on 1080p
default_final_pos = 1360, 560


def degrade():
    print("Degrading..")
    current_x, current_y = position()
    rightClick()
    moveTo(current_x - 10, current_y - 50)
    leftClick()
    moveTo(final_pos)
    leftClick()
    moveTo(current_x, current_y)
    print("Done")


def update_final_pos():
    global final_pos
    current_pos = position()
    final_pos = current_pos
    print("New Pos:", current_pos)


def check_hotkey():
    while 1:
        if is_pressed("shift+F8"):
            update_final_pos()
            sleep(0.1)
        elif is_pressed("F8"):
            degrade()
        elif is_pressed("F7"):
            print("Exiting..")
            exit()
        sleep(0.01)


if __name__ == '__main__':
    final_pos = default_final_pos
    check_hotkey()
