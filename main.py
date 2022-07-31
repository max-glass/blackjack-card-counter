# mxGlass
# Blackjack card counter (GUI)
 
# 30JUL2022
# mxGlass
# Fixed bug regarding log.insert().

# 30JUL2022
# mxGlass
# Added shuffle button.

import tkinter as tk
from tkinter import ttk
from unicodedata import numeric

# initialize variables
count = 0
num_cards = 0
log = []

def clicked(): # without event because I use `command=` instead of `bind`
    global count
    global num_cards

    count = count + 1
    num_cards = num_cards + 1

    label1.configure(text=f'Count = {count}')
    label2.configure(text=f'Cards Played = {num_cards}')

def clicked_null(): # without event because I use `command=` instead of `bind`
    global num_cards

    num_cards = num_cards + 1

    label2.configure(text=f'Cards Played = {num_cards}')

def clicked_neg():
    global count
    global num_cards

    count = count - 1
    num_cards = num_cards + 1

    label1.configure(text=f'Count = {count}')
    label2.configure(text=f'Cards Played = {num_cards}')

def add_log(x):
    global log
    log.insert(0, x)

def shuffle():
    global count
    global num_cards
    count = 0
    num_cards = 0
    label1.configure(text=f'Count = {count}')
    label2.configure(text=f'Cards Played = {num_cards}')



windows = tk.Tk()
windows.title("")

label = tk.Label(windows, text="Blackjack card counter")
label.grid(column=0, row=0)

logLabel = tk.Label(windows, text="Card log:")
logLabel.grid(column=1, row=10)

log = tk.Listbox()
log.grid(column=1, row=11)

label = tk.Label(windows, text="")
label.grid(column=4, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

label2 = tk.Label(windows)
label2.grid(column=1, row=1)

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

# Middle Cards
custom_button = ttk.Button(windows, text="7", command=lambda: [clicked_null(), add_log("7")])
custom_button.grid(column=1, row=2)

custom_button = ttk.Button(windows, text="8", command=lambda: [clicked_null(), add_log("8")])
custom_button.grid(column=1, row=3)

custom_button = ttk.Button(windows, text="9", command=lambda: [clicked_null(), add_log("9")])
custom_button.grid(column=1, row=4)

# Minus cards
custom_button = ttk.Button(windows, text="10", command=lambda: [clicked_neg(), add_log("10")])
custom_button.grid(column=2, row=2)

custom_button = ttk.Button(windows, text="J", command=lambda: [clicked_neg(), add_log("J")])
custom_button.grid(column=2, row=3)

custom_button = ttk.Button(windows, text="Q", command=lambda: [clicked_neg(), add_log("Q")])
custom_button.grid(column=2, row=4)

custom_button = ttk.Button(windows, text="K", command=lambda: [clicked_neg(), add_log("K")])
custom_button.grid(column=2, row=5)

custom_button = ttk.Button(windows, text="A", command=lambda: [clicked_neg(), add_log("A")])
custom_button.grid(column=2, row=6)

# Shuffle button
custom_button = ttk.Button(windows, text="Shuffle", command=lambda: [shuffle()])
custom_button.grid(column=1, row=7)

windows.mainloop()

