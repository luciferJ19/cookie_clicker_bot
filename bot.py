import pyautogui
import keyboard

if __name__ == "__main__":
    pyautogui.PAUSE = 0.0001

    x_coord = (14.7*pyautogui.size()[0])/100
    y_coord = (44.5*pyautogui.size()[1])/100
    pyautogui.sleep(8)
    while True:
        pyautogui.moveTo(x_coord, y_coord)
        pyautogui.click()
        if keyboard.is_pressed("q"):
            break