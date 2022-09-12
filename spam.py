import pyautogui
from tkinter import *
import time

warning = [
    "Spambot initilizing...",
    "Progress >> 10%", 
    "Progress >> 20%", 
    "Progress >> 60%", 
    "Progress >> 70%", 
    "Progress >> 90%",
    "Progress >> Complete \n Prepare for absolute destruction </o_o/>" 
]

def spamming():
    if spam_var.get() == 1:
        for i in warning:
            time.sleep(2)
            pyautogui.click(position)
            pyautogui.typewrite(i)
            pyautogui.typewrite(["enter"])
        time.sleep(7)
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
spam_var = IntVar()
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
checkbox_startsequence = Checkbutton(spam_screen, text="Warning sequence", variable=spam_var)
checkbox_startsequence.grid(row=5)
button_startspamming = Button(spam_screen, text="Start Spamming", command=spamming)
button_startspamming.grid(row=6)
label_position = Label(spam_screen, text=position)
label_position.grid(row=7)
button_selectposition = Button(spam_screen, text="Select Position", command=selectPosition)
button_selectposition.grid(row=8)

spam_screen.mainloop()
