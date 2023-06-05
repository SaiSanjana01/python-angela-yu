import os

#TODO-1: SHOW LOGO FROM art1.py
from art1 import logo


#TODO-2: ASK FOR USER NAME AND THE BID PRICE
#TODO-4: TO ASK THE USER IF THERE IS ANY OTHER BIDDERES
bids = {}
is_other_bidders=False

#TODO-5: TO FIND THE HIGHEST BID IN THE DICTIONARY AND DECLARE THEM AS WINNER
def secret_auction(highest_bid):
    high_bid=0
    winner = ""
    for bid in highest_bid:
        new_bid_price = highest_bid[bid]
        if new_bid_price > high_bid:
            high_bid = new_bid_price
            winner = bid
    print(f"The winner is {winner} and the highest bid amount is $ {high_bid}")

print(logo)
print("Welcome to the secret auction program!")

while not is_other_bidders:
    name = input("what is your name?: ")
    price = int(input("what is the bid price? $ "))
    bids[name] = price  #it is now the value of the key that is it'll check for the price

#TODO-3: TO CREATE AN EMPTY DICTIONARY AND NAME AS KEY AND BID AS VALUE

    should_continue= input("Type 'y' if there is other bidders else Type 'n'\n")
    if should_continue == 'n':
        is_other_bidders = True
        secret_auction(highest_bid = bids)
        #secret_auction(bids)
    elif should_continue == 'y':
        os.system('cls')













