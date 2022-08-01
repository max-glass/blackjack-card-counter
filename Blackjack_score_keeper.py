def main():
    global win
    global loss
    global push
    global diff
    global profit
    global balance

    win = 0
    loss = 0
    push = 0
    diff = 0
    profit = 0
    balance = 0

    print("\n")
    cash = input("What is your starting amount? ")


    def output():
        print("\n")
        print("Record (win, loss, push):",win,"-",loss,"-",push)
        print("\n")
        print("Balance:",balance)
        print("\n")
        print("Session P/L:",diff)

    while 1 == 1:
        print("_____________________________________")
        print("\n")
        record = input("Was the last hand won or lost? ")
        if record == "w":
            win = win + 1
            bet_amt = input("Was the bet amount? ")
            int(bet_amt)
            int(cash)
            diff = diff + int(bet_amt)
            profit = profit + int(bet_amt)
            balance = profit + int(cash)
            output()

        if record == "l":
            loss = loss + 1
            bet_amt = input("Was the bet amount? ")

            int(bet_amt)
            int(cash)
            diff = diff - int(bet_amt)
            profit = profit - int(bet_amt)
            balance = profit + int(cash)
            output()

        if record == "stats":
            output()

        if record == "adj":
            adj = input("How much would you want to adjust? ")
            print("Current cash: ",cash)
            int(adj)
            cash = int(cash) + int(adj)
            output()
            
        if record == "p":
            push = push +1
            #bet_amt = input("Was the bet amount? ")
            #cash = int(cash) + int(bet_amt)
            output()
            continue

main()