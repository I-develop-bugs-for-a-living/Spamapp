import pyautogui
from tkinter import *
import time


def spamming():
    if count_var.get:
        for i in range(count_var.get()):
            time.sleep(0.05)
            pyautogui.click(-1231, 979)
            pyautogui.typewrite(name_var.get())
            pyautogui.typewrite(["enter"])
    else:
        while True:
            time.sleep(4)
            pyautogui.click(-1231, 979)
            pyautogui.typewrite(name_var.get())
            pyautogui.typewrite(["enter"])

print(pyautogui.position())
#Point(x=-1208, y=1014)
spam_screen = Tk()
count_var = IntVar()
name_var = StringVar()
spam_screen.title("SpamBot")
l = Label(spam_screen, text="SpamBot", font=("Arial", 20))
l.grid(row=0, columnspan=3)
l1 = Label(text="Enter the phrase to spam:")
l1.grid(row=1)
en = Entry(textvariable=name_var)
en.grid(row=2)
l2 = Label(spam_screen, text="How many times should the msg be send?")
l2.grid(row=3)
en1 = Entry(spam_screen, textvariable=count_var)
en1.grid(row=4)
a = Button(spam_screen, text="Start Spamming", command=spamming)
a.grid(row=5)

spam_screen.mainloop()
