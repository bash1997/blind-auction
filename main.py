from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))

def winner(bidders):
    dictionary = bidders
    highest_key = ""
    highest_value = 0
    for bids in dictionary:
        if dictionary[bids] > highest_value:
            highest_key = bids
            highest_value = dictionary[bids]
    print(f"The highest bidder was {highest_key}, who put in a bid of ${highest_value}")

def blind_auction(name, bid):
    live_bid = {}
    live_bid[name] = bid
    cont = input("Are there anymore bidders?: Yes/No: ").lower()
    more = True

    while more == True:
        clear()
        if cont == "yes":
            more = True
            name = input("What is your name?: ")
            bid = int(input("What's your bid?: $"))
            live_bid[name] = bid
            cont = input("Are there anymore bidders?: Yes/No: ").lower()

        elif cont == "no":
            winner(live_bid)
            more = False
blind_auction(name, bid)

run_again = input("Run again? Yes/No: ").lower
and_again = True

while and_again == True:
    
    clear()
    print(logo)
    
    if run_again != "yes":
        and_again = False
    else:
        live_bid = {}
        name = input("What is your name?: ")   
        bid = int(input("What's your bid?: $"))
        more = True
        blind_auction(name, bid)

        run_again = input("Run again? Yes/No: ").lower
    
