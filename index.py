import pyautogui
import time


seta_herois = (685, 747)
herois = (659, 708)
work_button = (507, 645)
rest_button = (586, 246)
close_herois_button = (690, 142)

def close_herois():
    pyautogui.click(close_herois_button)
    time.sleep(1)
    pyautogui.click(670, 414)
    time.sleep(1)

def main():
    print("Coloque o foco na tela do bomb...")
    time.sleep(2)

    pyautogui.click(seta_herois)

    time.sleep(1)

    pyautogui.click(herois)

    time.sleep(10)

    pyautogui.click(337, 413)

    # Coloca os bonecos pra descansar
    for num in range(0, 12):
        pyautogui.click(rest_button)
        time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.scroll(-100)

    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.scroll(-100)

    time.sleep(1)

    # Coloca os bonecos pra trabalhar
    for num in range(0, 12):
        pyautogui.click(work_button)
        time.sleep(1)

while True:
    main()
    close_herois()
    time.sleep(120+60)
