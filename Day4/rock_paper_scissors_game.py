import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What is your choice?\n[0] ROCK\n[1] PAPER\n[2] SCISSORS?\n"))
random = random.randint(0, 2)

if user == 0:
    if random == 0:
        print(f"You chose:\n{rock}\nAI Chose:\n{rock}\nTied Game!")
    elif random == 1:
        print(f"You chose:\n{rock}\nAI Chose:\n{paper}\nYou Lose!")
    else:
        print(f"You chose:\n{rock}\n\nAI Chose:\n{scissors}\nYou Win!")
elif user == 1:
    if random == 0:
        print(f"You chose:\n{paper}\nAI Chose:\n{rock}\nYou Win!")
    elif random == 1:
        print(f"You chose:\n{paper}\nAI Chose:\n{paper}\nTied Game!")
    else:
        print(f"You chose:\n{paper}\nAI Chose:\n{scissors}\nYou Lose!")
elif user == 2:
    if random == 0:
        print(f"You chose:\n{scissors}\n\nAI Chose:\n{rock}\nYou Lose!")
    elif random == 1:
        print(f"You chose:\n{scissors}\nAI Chose:\n{paper}\nYou Win!")
    else:
        print(f"You chose:\n{scissors}\nAI Chose:\n{scissors}\nTied Game!")
else:
    print("Hey, you have to select between the numbers 0, 1 and 2. Try Again!")
