import pyautogui
from tkinter import *
import time


def spamming():
    if count_var.get:
        for i in range(count_var.get()):
            time.sleep(0.05)
            pyautogui.click(position)
            pyautogui.typewrite(name_var.get())
            pyautogui.typewrite(["enter"])
    else:
        while True:
            time.sleep(4)
            pyautogui.click(position)
            pyautogui.typewrite(name_var.get())
            pyautogui.typewrite(["enter"])

def selectPosition():
    global position
    time.sleep(2)
    position = pyautogui.position()
    label_position.config(text=position)

position = (-1231, 979)
spam_screen = Tk()
count_var = IntVar()
name_var = StringVar()
spam_screen.title("SpamBot")
label_header = Label(spam_screen, text="SpamBot", font=("Arial", 20))
label_header.grid(row=0, columnspan=3)
label_forentry_spamphrase = Label(text="Enter the phrase to spam:")
label_forentry_spamphrase.grid(row=1)
entry_spamphrase = Entry(textvariable=name_var)
entry_spamphrase.grid(row=2)
label_forentry_iterations = Label(spam_screen, text="Amount?")
label_forentry_iterations.grid(row=3)
entry_iterations = Entry(spam_screen, textvariable=count_var)
entry_iterations.grid(row=4)
button_startspamming = Button(spam_screen, text="Start Spamming", command=spamming)
button_startspamming.grid(row=5)
label_position = Label(spam_screen, text=position)
label_position.grid(row=6)
button_selectposition = Button(spam_screen, text="Select Position", command=selectPosition)
button_selectposition.grid(row=7)

spam_screen.mainloop()
