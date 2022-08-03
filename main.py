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
# Added win/loss score keeper.

# 31JUL2022
# the_BigMike_
# Added variable number of decks


# TODO: Implement win/loss script into GUI (mxGlass).
# TODO: Make font bigger on GUI.
# TODO: Determine formula/function to predict good bet amount (taking account of record, balance, count, etc.).
# TODO: Clear win/loss fields after clicking "calculate."
# TODO: Maybe we link this to hardware? ... Think about it.


# Import necessary libraries
# External dependencies
import enum
from re import T
import tkinter as tk
from tkinter import Label, ttk, messagebox
from tkinter import *
from turtle import width
from unicodedata import numeric
# from Blackjack_score_keeper import main

# System dependencies
import os
import subprocess
import threading

from strategy import basic_strategy

# Initialize variables
count = 0
numCards = 0
log = []
numDecks = 8
cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
cardsRemaining = [0,0,0,0,0,0,0,0,0,0,0,0,0]



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
# Update number of decks
def deckInput():
    global numDecks
    inp = decksInput.get(1.0, "end-1c")
    numDecks = int(inp)
    decksLabel.configure(text=f'Number of decks: {numDecks}')
    label3.configure(text=f'True Count = {trueCount()}')
    remaining()

def strategy():
    playerValue = []
    soft = False
    player = playerInput.get(1.0, "end-1c").split(',')
    dealer = dealerInput.get(1.0, "end-1c")
    match(dealer.lower()):
        case "a":
            dealerValue = 1
        case "k" | "q" | 'j':
            dealerValue = 10
        case _:
            dealerValue = int(dealer)
    for i, card in enumerate(player):
        match(player[i].lower()):
            case "a":
                playerValue.append(11)
                soft = True
            case "k" | "q" | 'j':
                playerValue.append(10)
            case _:
                playerValue.append(int(player[i]))
    label4.configure(text=f'What to do: {basic_strategy(sum(playerValue), dealerValue, soft)}')
    

#calculates the number of remaining cards for each value
def remaining():
    for i, card in enumerate(cards):
        cardsRemaining[i] = 4*numDecks
    remainingA.configure(text=f"A: {cardsRemaining[0]}")
    remainingK.configure(text=f"K: {cardsRemaining[1]}")
    remainingQ.configure(text=f"Q: {cardsRemaining[2]}")
    remainingJ.configure(text=f"J: {cardsRemaining[3]}")
    remaining10.configure(text=f"10: {cardsRemaining[4]}")
    remaining9.configure(text=f"9: {cardsRemaining[5]}")
    remaining8.configure(text=f"8: {cardsRemaining[6]}")
    remaining7.configure(text=f"7: {cardsRemaining[7]}")
    remaining6.configure(text=f"6: {cardsRemaining[8]}")
    remaining5.configure(text=f"5: {cardsRemaining[9]}")
    remaining4.configure(text=f"4: {cardsRemaining[10]}")
    remaining2.configure(text=f"2: {cardsRemaining[12]}")
    remaining3.configure(text=f"3: {cardsRemaining[11]}")

# Calculate the true count
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
    match(x):
        case "A":
            cardsRemaining[0] = cardsRemaining[0]-1
            remainingA.configure(text=f"A: {cardsRemaining[0]}")
        case "K":
            cardsRemaining[1] = cardsRemaining[1]-1
            remainingK.configure(text=f"K: {cardsRemaining[1]}")
        case "Q":
            cardsRemaining[2] = cardsRemaining[2]-1
            remainingQ.configure(text=f"Q: {cardsRemaining[2]}")
        case "J":
            cardsRemaining[3] = cardsRemaining[3]-1
            remainingJ.configure(text=f"J: {cardsRemaining[3]}")
        case "10":
            cardsRemaining[4] = cardsRemaining[4]-1
            remaining10.configure(text=f"10: {cardsRemaining[4]}")
        case "9":
            cardsRemaining[5] = cardsRemaining[5]-1
            remaining9.configure(text=f"9: {cardsRemaining[5]}")
        case "8":
            cardsRemaining[6] = cardsRemaining[6]-1
            remaining8.configure(text=f"8: {cardsRemaining[6]}")
        case "7":
            cardsRemaining[7] = cardsRemaining[7]-1
            remaining7.configure(text=f"7: {cardsRemaining[7]}")
        case "6":
            cardsRemaining[8] = cardsRemaining[8]-1
            remaining6.configure(text=f"6: {cardsRemaining[8]}")
        case "5":
            cardsRemaining[9] = cardsRemaining[9]-1
            remaining5.configure(text=f"5: {cardsRemaining[9]}")
        case "4":
            cardsRemaining[10] = cardsRemaining[10]-1
            remaining4.configure(text=f"4: {cardsRemaining[10]}")
        case "3":
            cardsRemaining[11] = cardsRemaining[11]-1
            remaining3.configure(text=f"3: {cardsRemaining[11]}")
        case "2":
            cardsRemaining[12] = cardsRemaining[12]-1
            remaining2.configure(text=f"2: {cardsRemaining[12]}")

# Shuffle and reset count
def shuffle():
    global count
    global numCards
    count = 0
    numCards = 0
    label1.configure(text=f'Count = {count}')
    label2.configure(text=f'Cards Played = {numCards}')
    label3.configure(text=f'True Count = {trueCount()}')
    remaining()

# initiate the number of cards based on the number of decks
for i, card in enumerate(cards):
    cardsRemaining[i] = 4*numDecks

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

label4 = tk.Label(windows, text="What to do: ")
label4.grid(column=2, row=12)

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


# Win/Loss
newButton = ttk.Button(windows, text='Win/Loss', command=win_loss)
newButton.grid(row=11, column=0)

# Deck Input
decksLabel = tk.Label(windows, text=f"Number of decks: {numDecks}")
decksLabel.grid(column=0, row=8)
decksInput = tk.Text(windows, height = 1, width = 5)
decksInput.grid(column=0, row=9)
custom_button = ttk.Button(windows, text="Update", command=lambda: [deckInput()])
custom_button.grid(column=0, row=10)

# Dealer Input
dealerLabel = tk.Label(windows, text=f"Dealer Card:", height=1)
dealerLabel.grid(column=0, row=12)
dealerInput = tk.Text(windows, height = 1, width = 10)
dealerInput.grid(column=0, row=13)

# Player Input
playerLabel = tk.Label(windows, text=f"Player Cards")
playerLabel.grid(column=1, row=12)
playerInput = tk.Text(windows, height = 1, width = 10)
playerInput.grid(column=1, row=13)
custom_button = ttk.Button(windows, text="Update", command=lambda: [strategy()])
custom_button.grid(column=1, row=14)

# Number of cards remaining
remainingA = tk.Label(windows, text=f"A: {cardsRemaining[0]}")
remainingA.grid(column=3, row=2)
remainingK = tk.Label(windows, text=f"K: {cardsRemaining[1]}")
remainingK.grid(column=3, row=3)
remainingQ = tk.Label(windows, text=f"Q: {cardsRemaining[2]}")
remainingQ.grid(column=3, row=4)
remainingJ = tk.Label(windows, text=f"J: {cardsRemaining[3]}")
remainingJ.grid(column=3, row=5)
remaining10 = tk.Label(windows, text=f"10: {cardsRemaining[4]}")
remaining10.grid(column=3, row=6)
remaining9 = tk.Label(windows, text=f"9: {cardsRemaining[5]}")
remaining9.grid(column=3, row=7)
remaining8 = tk.Label(windows, text=f"8: {cardsRemaining[6]}")
remaining8.grid(column=3, row=8)
remaining7 = tk.Label(windows, text=f"7: {cardsRemaining[7]}")
remaining7.grid(column=3, row=9)
remaining6 = tk.Label(windows, text=f"6: {cardsRemaining[8]}")
remaining6.grid(column=4, row=2)
remaining5 = tk.Label(windows, text=f"5: {cardsRemaining[9]}")
remaining5.grid(column=4, row=3)
remaining4 = tk.Label(windows, text=f"4: {cardsRemaining[10]}")
remaining4.grid(column=4, row=4)
remaining3 = tk.Label(windows, text=f"3: {cardsRemaining[11]}")
remaining3.grid(column=4, row=5)
remaining2 = tk.Label(windows, text=f"2: {cardsRemaining[12]}")
remaining2.grid(column=4, row=6)

windows.mainloop()