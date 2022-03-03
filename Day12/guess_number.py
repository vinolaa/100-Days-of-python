import random

def play_game():
    chances = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number = random.randint(1, 100)
    if difficulty == "easy":
        chances = 10
    elif difficulty == "hard":
        chances = 5
    for n in range(chances):
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You Win!")
            return
        elif guess > number:
            print("Too high.")
            chances -= 1
        else:
            print("Too low.")
            chances -= 1
    if chances == 0:
        print(f"Sorry, you lose. The correct number was {number}.")

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
keep = True
while keep:
    play_game()
    keep_playing = int(input("Do you want to play again? Type:\n[1] - YES\n[2] - NO\n"))
    if keep_playing == 2:
        print("GoodBye!")
        keep = False
