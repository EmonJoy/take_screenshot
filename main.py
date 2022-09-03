import pyautogui
import time
time.sleep(1)
print("*********** welcome to screenshot taker ****************")
ss = pyautogui.screenshot()
a = input("saving ss by: ")
ss.save(f"E:\\{a}")
print("Created by Emon Joy")
