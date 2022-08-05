"""
Main file for Blackjack card counter. Keeps track of the cards played, Count, and True Count
"""

import tkinter as tk
from tkinter import Toplevel, ttk
from logger import logger
from strategy import basic_strategy


class Blackjack:
    """
    Class to keep track and update variables within the application
    """

    def __init__(self):
        self.count = 0
        self.num_cards = 0
        self.num_decks = 6
        self.cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.cash = 0
        self.win = 0
        self.loss = 0
        self.push = 0
        self.diff = 0
        self.window = tk.Tk()
        self.log_area = tk.Label()
        self.count_label = tk.Label()
        self.true_count_label = tk.Label()
        self.cards_played_label = tk.Label()
        self.decks_label = tk.Label()
        self.decks_input = tk.Text()
        self.dealer_label = tk.Label()
        self.dealer_input = tk.Text()
        self.player_label = tk.Label()
        self.player_input = tk.Text()
        self.action_label = tk.Label()

    def clicked(self, card):
        """
        Runs when a low card is dealt (2-6) to keep track of the
        count/true count and add number to the log
        """
        self.count = self.count + 1
        self.num_cards = self.num_cards + 1

        self.count_label.configure(text=f"Count: {self.count}")
        self.true_count_label.configure(text=f"True Count: {self.true_count()}")
        self.cards_played_label.configure(text=f"Cards Played: {self.num_cards}")

        self.log_area.insert(0, card)
        logger(card)

    def clicked_null(self, card):
        """
        Runs when a middle card is dealt (7-9) to keep track of the
        count/true count and add number to the log
        """
        self.num_cards = self.num_cards + 1

        self.count_label.configure(text=f"Count: {self.count}")
        self.true_count_label.configure(text=f"True Count: {self.true_count()}")
        self.cards_played_label.configure(text=f"Cards Played: {self.num_cards}")

        self.log_area.insert(0, card)
        logger(card)

    def clicked_neg(self, card):
        """
        Runs when a high card is dealt (9-A) to keep track of the
        count/true count and add number to the log
        """
        self.count = self.count - 1
        self.num_cards = self.num_cards + 1

        self.count_label.configure(text=f"Count: {self.count}")
        self.true_count_label.configure(text=f"True Count: {self.true_count()}")
        self.cards_played_label.configure(text=f"Cards Played: {self.num_cards}")

        self.log_area.insert(0, card)
        logger(card)

    def true_count(self):
        """
        Calculates the true count when a card is dealt.
        Detemined by the count/number of remaining decks
        """
        return round(self.count / (((52 * self.num_decks) - self.num_cards) / 52))

    def shuffle(self):
        """
        Resets the count/true count, and number of cards played to 0
        Run when the shoe is changed
        """
        self.count = 0
        self.num_cards = 0

        self.count_label.configure(text=f"Count: {self.count}")
        self.true_count_label.configure(text=f"True Count: {self.true_count()}")
        self.cards_played_label.configure(text=f"Cards Played: {self.num_cards}")
        self.log_area.delete(0, "end")

    def deck_input(self):
        """
        Allows user to update the number of decks being played
        Increases the accuracy of the true count
        """
        self.num_decks = int(self.decks_input.get(1.0, "end-1c"))

        self.decks_label.configure(text=f"Number of Decks: {self.num_decks}")
        self.true_count_label.configure(text=f"True Count: {self.true_count()}")

    def strategy(self):
        """
        User inputs the dealer/player cards and is given the correct action to take
        """
        player_value = []
        soft = False
        player = self.player_input.get(1.0, "end-1c").split(",")
        dealer = self.dealer_input.get(1.0, "end-1c")

        match (dealer.lower()):
            case "a":
                dealer_value = 1
            case "k" | "q" | "j":
                dealer_value = 10
            case _:
                dealer_value = int(dealer)

        for card in player:
            match (card.lower()):
                case "a":
                    player_value.append(11)
                    soft = True
                case "k" | "q" | "j":
                    player_value.append(10)
                case _:
                    player_value.append(int(card))

        self.action_label.configure(
            text=f"What to do: {basic_strategy(sum(player_value), dealer_value, soft)}"
        )

    def win_loss(self):
        """
        Tracks the wins and losses for the session
        """
        new_window = Toplevel(self.window)

        tk.Label(new_window, text="What is your starting amount?").grid(row=0)
        initial_cash = tk.Entry(new_window)
        initial_cash.grid(row=0, column=1)

        tk.Label(new_window, text="Was the last hand won or lost?").grid(row=1)
        record = tk.Entry(new_window)
        record.grid(row=1, column=1)

        tk.Label(new_window, text="What was the bet amount ?").grid(row=2)
        bet_amt = tk.Entry(new_window)
        bet_amt.grid(row=2, column=1)

        def output(self):
            """
            Calculates the output of the calculations for win/loss
            """
            if self.win + self.loss + self.push == 0:
                self.cash = int(initial_cash.get())
            trecord = str(record.get())
            tbet_amt = int(bet_amt.get())

            if trecord == "w":
                self.win = self.win + 1
                self.cash = int(self.cash) + int(tbet_amt)
                self.diff = self.diff + int(tbet_amt)
            elif trecord == "l":
                self.loss = self.loss + 1
                int(tbet_amt)
                self.cash = int(self.cash) - int(tbet_amt)
                self.diff = self.diff - int(tbet_amt)
            elif trecord == "p":
                self.push = self.push + 1

            tk.Label(
                new_window,
                text=f"Record (win, loss, push): {self.win} - {self.loss} - {self.push}",
            ).grid(row=4)
            tk.Label(new_window, text=f"Balance: {self.cash}").grid(row=5)
            tk.Label(new_window, text=f"Session P/L: {self.diff}").grid(row=6)

        custom_button = tk.Button(
            new_window, text="Calculate", command=lambda: [output(self)]
        )
        custom_button.grid(row=3, column=0)


def main():
    """
    Main window of the blackjack card counter application
    """
    blackjack = Blackjack()
    blackjack.window.title("Card Counter")

    label = tk.Label(blackjack.window, text="Blackjack card counter")
    label.grid(column=0, row=0)

    log_label = tk.Label(blackjack.window, text="Card Log:")
    log_label.grid(column=1, row=10)

    blackjack.log_area = tk.Listbox(blackjack.window)
    blackjack.log_area.grid(column=1, row=11)

    blackjack.count_label = tk.Label(blackjack.window, text="Count:")
    blackjack.count_label.grid(column=0, row=1)

    blackjack.true_count_label = tk.Label(blackjack.window, text="True Count:")
    blackjack.true_count_label.grid(column=1, row=1)

    blackjack.cards_played_label = tk.Label(blackjack.window, text="Cards Played:")
    blackjack.cards_played_label.grid(column=2, row=1)

    # Shuffle button
    custom_button = ttk.Button(
        blackjack.window, text="Shuffle", command=lambda: [blackjack.shuffle()]
    )
    custom_button.grid(column=1, row=7)

    # Plus cards
    custom_button = ttk.Button(
        blackjack.window, text="2", command=lambda: [blackjack.clicked("2")]
    )
    custom_button.grid(column=0, row=2)
    custom_button = ttk.Button(
        blackjack.window, text="3", command=lambda: [blackjack.clicked("3")]
    )
    custom_button.grid(column=0, row=3)
    custom_button = ttk.Button(
        blackjack.window, text="4", command=lambda: [blackjack.clicked("4")]
    )
    custom_button.grid(column=0, row=4)
    custom_button = ttk.Button(
        blackjack.window, text="5", command=lambda: [blackjack.clicked("5")]
    )
    custom_button.grid(column=0, row=5)
    custom_button = ttk.Button(
        blackjack.window, text="6", command=lambda: [blackjack.clicked("6")]
    )
    custom_button.grid(column=0, row=6)

    # Middle Cards
    custom_button = ttk.Button(
        blackjack.window, text="7", command=lambda: [blackjack.clicked_null("7")]
    )
    custom_button.grid(column=1, row=2)
    custom_button = ttk.Button(
        blackjack.window, text="8", command=lambda: [blackjack.clicked_null("8")]
    )
    custom_button.grid(column=1, row=3)
    custom_button = ttk.Button(
        blackjack.window, text="9", command=lambda: [blackjack.clicked_null("9")]
    )
    custom_button.grid(column=1, row=4)

    # Minus cards
    custom_button = ttk.Button(
        blackjack.window, text="10", command=lambda: [blackjack.clicked_neg("10")]
    )
    custom_button.grid(column=2, row=2)
    custom_button = ttk.Button(
        blackjack.window, text="J", command=lambda: [blackjack.clicked_neg("J")]
    )
    custom_button.grid(column=2, row=3)
    custom_button = ttk.Button(
        blackjack.window, text="Q", command=lambda: [blackjack.clicked_neg("Q")]
    )
    custom_button.grid(column=2, row=4)
    custom_button = ttk.Button(
        blackjack.window, text="K", command=lambda: [blackjack.clicked_neg("K")]
    )
    custom_button.grid(column=2, row=5)
    custom_button = ttk.Button(
        blackjack.window, text="A", command=lambda: [blackjack.clicked_neg("A")]
    )
    custom_button.grid(column=2, row=6)

    # Deck Input
    blackjack.decks_label = tk.Label(
        blackjack.window, text=f"Number of Decks: {blackjack.num_decks}"
    )
    blackjack.decks_label.grid(column=0, row=8)
    blackjack.decks_input = tk.Text(blackjack.window, height=1, width=5)
    blackjack.decks_input.grid(column=0, row=9)
    custom_button = ttk.Button(
        blackjack.window, text="Update", command=lambda: [blackjack.deck_input()]
    )
    custom_button.grid(column=0, row=10)

    # Dealer Input
    blackjack.dealer_label = tk.Label(blackjack.window, text="Dealer Card:")
    blackjack.dealer_label.grid(column=0, row=12)
    blackjack.dealer_input = tk.Text(blackjack.window, height=1, width=10)
    blackjack.dealer_input.grid(column=0, row=13)

    # Player Input
    blackjack.player_label = tk.Label(blackjack.window, text="Player Cards:")
    blackjack.player_label.grid(column=1, row=12)
    blackjack.player_input = tk.Text(blackjack.window, height=1, width=10)
    blackjack.player_input.grid(column=1, row=13)
    custom_button = ttk.Button(
        blackjack.window, text="Update", command=lambda: [blackjack.strategy()]
    )
    custom_button.grid(column=1, row=14)

    # What action to take
    blackjack.action_label = tk.Label(blackjack.window, text="What to do: ")
    blackjack.action_label.grid(column=2, row=12)

    win_loss_button = ttk.Button(
        blackjack.window, text="Win/Loss", command=blackjack.win_loss
    )
    win_loss_button.grid(row=11, column=0)

    blackjack.window.mainloop()


if __name__ == "__main__":
    main()
