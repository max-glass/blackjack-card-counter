# mxGlass
# Blackjack card counter (GUI)
 
# 30JUL2022
# mxGlass
# Fixed bug regarding log.insert()

import tkinter as tk
from tkinter import ttk

# initialize variables
count = 0
log = []

def clicked(): # without event because I use `command=` instead of `bind`
    global count

    count = count + 1

    label1.configure(text=f'Count = {count}')

def clicked_neg():
    global count

    count = count - 1

    label1.configure(text=f'Count = {count}')

def add_log(x):
    global log
    log.insert(0, x)


windows = tk.Tk()
windows.title("")

label = tk.Label(windows, text="Blackjack card counter")
label.grid(column=0, row=0)

logLabel = tk.Label(windows, text="Card log:")
logLabel.grid(column=2, row=10)

log = tk.Listbox()
log.grid(column=2, row=11)

label = tk.Label(windows, text="")
label.grid(column=4, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

# Plus cards
custom_button = ttk.Button(windows, text="2", command=lambda: [clicked(), add_log("2")])
custom_button.grid(column=0, row=2)

custom_button = ttk.Button(windows, text="3", command=lambda: [clicked(), add_log("3")])
custom_button.grid(column=0, row=3)

custom_button = ttk.Button(windows, text="4", command=lambda: [clicked(), add_log("4")])
custom_button.grid(column=0, row=4)

custom_button = ttk.Button(windows, text="5", command=lambda: [clicked(), add_log("5")])
custom_button.grid(column=0, row=5)

custom_button = ttk.Button(windows, text="6", command=lambda: [clicked(), add_log("6")])
custom_button.grid(column=0, row=6)

# Minus cards
custom_button = ttk.Button(windows, text="10", command=lambda: [clicked_neg(), add_log("10")])
custom_button.grid(column=1, row=2)

custom_button = ttk.Button(windows, text="J", command=lambda: [clicked_neg(), add_log("J")])
custom_button.grid(column=1, row=3)

custom_button = ttk.Button(windows, text="Q", command=lambda: [clicked_neg(), add_log("Q")])
custom_button.grid(column=1, row=4)

custom_button = ttk.Button(windows, text="K", command=lambda: [clicked_neg(), add_log("K")])
custom_button.grid(column=1, row=5)

custom_button = ttk.Button(windows, text="A", command=lambda: [clicked_neg(), add_log("A")])
custom_button.grid(column=1, row=6)

windows.mainloop()

