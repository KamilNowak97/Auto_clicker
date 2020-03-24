import pyautogui as clicker
import time

time_set = int(input("Write for how many seconds the program will work."))
print("Position the cursor where the program will click. You have 5 seconds.")
time.sleep(2)
x,y = clicker.position()
print("It's time to click!")

time_start = time.time()
while time.time() < time_start + time_set:
    clicker.click(x, y)
    clicker.PAUSE = 0.001


