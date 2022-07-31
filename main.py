# mxGlass
# Blackjack card counter (GUI)
 
# 30JUL2022
# mxGlass
# Fixed bug regarding log.insert().

# 30JUL2022
# mxGlass
# Added shuffle button.

# 30JUL2022
# the_BigMike_
# Added number of cards and true count.

# 31JUL2022
# kilixn
# Added win / loss score keeper.

# TODO: Make amount of decks variable.
# TODO: Implement win/loss script into GUI (mxGlass). 
# TODO: Determine formula/function to predict good bet amount (taking account of record, balance, count, etc.).
# TODO: Maybe we link this to hardware? ... Think about it.

# Import necessary libraries
# External dependencies
import tkinter as tk
from tkinter import Label, ttk, messagebox
from tkinter import *
from unicodedata import numeric
# from Blackjack_score_keeper import main

# System dependencies
import os
import subprocess
import threading

# Initialize variables
count = 0
numCards = 0
log = []
numDecks = 8

# Win/loss
# global win
# global loss
# global push
# global diff
# win = 0
# loss = 0
# push = 0
# diff = 0

# Define and calculate true count (the_BigMike_)
def trueCount():
    return round(count/(((52*numDecks)-numCards)/52))

# Define when "clicked"
def clicked(): # without event because I use `command=` instead of `bind`
    global count
    global numCards

    count = count + 1
    numCards = numCards + 1

    label1.configure(text=f'Count = {count}')
    label2.configure(text=f'Cards Played = {numCards}')
    label3.configure(text=f'True Count = {trueCount()}')

def clicked_null(): # without event because I use `command=` instead of `bind`
    global numCards

    numCards = numCards + 1

    label2.configure(text=f'Cards Played = {numCards}')
    label3.configure(text=f'True Count = {trueCount()}')

def clicked_neg():
    global count
    global numCards

    count = count - 1
    numCards = numCards + 1

    label1.configure(text=f'Count = {count}')
    label2.configure(text=f'Cards Played = {numCards}')
    label3.configure(text=f'True Count = {trueCount()}')

# Logging
def add_log(x):
    global log
    log.insert(0, x)

# Shuffle and reset count
def shuffle():
    global count
    global numCards
    count = 0
    numCards = 0
    label1.configure(text=f'Count = {count}')
    label2.configure(text=f'Cards Played = {numCards}')
    label3.configure(text=f'True Count = {trueCount()}')

def win_loss():
    newWindow = Toplevel(windows)
    global win
    global loss
    global push
    global diff
    global cash
    cash = 0
    win = 0
    loss = 0
    push = 0
    diff = 0
    
    def output():
        global win
        global loss
        global push
        global diff
      
        tcash = int(cash.get())
        trecord = str(record.get())
        tbet_amt = int(bet_amt.get())

        if trecord == "w":
            win = win + 1
            int(tbet_amt)
            tcash = int(tcash) + int(tbet_amt)
            diff = diff + int(tbet_amt)
        
        if trecord == "l":
            loss = loss + 1
            int(tbet_amt)
            tcash = int(tcash) - int(tbet_amt)
            diff = diff - int(tbet_amt)
        
        tk.Label(newWindow, text=f"Record (win, loss, push):{win} - {loss} - {push}").grid(row=4)
        tk.Label(newWindow, text=f"Balance: {tcash}").grid(row=5)
        tk.Label(newWindow, text=f"Session P/L:: {diff}").grid(row=6)

    tk.Label(newWindow, text="What is your starting amount?").grid(row=0)
    cash = tk.Entry(newWindow)
    cash.grid(row=0, column=1)

    tk.Label(newWindow, text="Was the last hand won or lost?").grid(row=1)
    record = tk.Entry(newWindow)
    record.grid(row=1, column=1)

    tk.Label(newWindow, text="What was the bet amount ?").grid(row=2)
    bet_amt = tk.Entry(newWindow)
    bet_amt.grid(row=2, column=1)

    custom_button = tk.Button(newWindow, text="calculate", command=output)
    custom_button.grid(row = 3, column=0)    

# GUI stuff below
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
label2.grid(column=2, row=1)

label3 = tk.Label(windows)
label3.grid(column=1, row=1)

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

# Win / Loss
newButton = ttk.Button(windows, text='Win/Loss', command=win_loss)
newButton.grid(row=11, column=0)

windows.mainloop()