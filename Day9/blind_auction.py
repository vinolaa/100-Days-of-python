from Modulos import day9

print(day9.logo + "\nWelcome to the secret auction program.")

people_in = {}

def find_winner(bids):
    highest_bid = 0
    winner = ""
    for key in bids:
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            winner = key
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")

keep = True
while keep:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    people_in[name] = bid
    option = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if option == 'no':
        keep = False
        find_winner(people_in)
