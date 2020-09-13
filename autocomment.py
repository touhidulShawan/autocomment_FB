import pyautogui
import time

# list all of your comments
all_comments = ["This is great", "Wonderful Picture"]

time.sleep(5)

for i in range(10000):
    # replace 2 with total item in all_comments array
    pyautogui.typewrite(all_comments[i % 2])
    pyautogui.typewrite("\n")
    time.sleep(3)
