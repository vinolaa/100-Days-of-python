from Modulos.bjack import logo
import random

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calc_score(hand):
    score = sum(hand)
    if score > 21:
        return 0
    return score

def change_ace(hand):
    score = calc_score(hand)
    if score > 21:
        for card in hand:
            if card == 11:
                hand.remove(11)
                hand.append(1)

def winner(player, dealer):
    if sum(player) > sum(dealer):
        return "\nCongrats! You win."
    elif sum(dealer) > 21:
        return "\nCongrats! You win."
    elif sum(player) < sum(dealer):
        return "\nSorry! You lose."
    elif sum(player) == sum(dealer):
        return "\nThat is a draw."

def dealer_draw(player, dealer):
    while sum(dealer) < sum(player):
        dealer.append(draw_card())
        change_ace(dealer)

def show_score(player, dealer):
    print(f"Your Hand: {player} || Your Score: {sum(player)}\nDealer Hand: {dealer} || Dealer Score: {sum(dealer)}")

def start_game(player, dealer):
    print(logo)
    for _ in range(2):
        player.append(draw_card())
    dealer.append(draw_card())
    change_ace(player)
    change_ace(dealer)
    show_score(player_hand, dealer_hand)

if input("Do you want to play blackjack? Type 'y' or 'n': ").lower() == 'y':
    player_hand = []
    dealer_hand = []
    start_game(player_hand, dealer_hand)
    keep = True
    while keep:
        if input("Keep playing? Type 'y' or 'n': ").lower() == "y":
            player_hand.append(draw_card())
            change_ace(player_hand)
            if calc_score(player_hand) == 0:
                show_score(player_hand, dealer_hand)
                print("\nSorry! You lost because got more than 21. ")
                keep = False
            else:
                show_score(player_hand, dealer_hand)
        else:
            dealer_draw(player_hand, dealer_hand)
            show_score(player_hand, dealer_hand)
            print(winner(player_hand, dealer_hand))
            keep = False
