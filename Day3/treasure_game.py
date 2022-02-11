print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side = input("\nYou see a sign with two way, LEFT or RIGHT, which side do you choose? ").lower()
if side == "right":
    print("\nGame Over! You fell from a 100m hole.")
else:
    lake = input("\nYou chose the correct way. But some miles away you saw a big lake. You have two options, "
                 "SWIM the lake or WAIT a boat. What are you going to do? ").lower()
    if lake == "swim":
        print("\nGame Over! A shark attacked you.")
    else:
        door = input("\nWhen you crossed the lake, a house was waiting for you. But, there where three options of"
                     "doors for you. A RED door, a BLUE door and a YELLOW door. Which color you choose? ").lower()
        if door == "red":
            print("\nGame Over! The door had a fire trap and you burned.")
        elif door == "blue":
            print("\nGame Over! The door had beasts and you got eaten.")
        elif door == "yellow":
            print("\nCONGRATULATIONS! You found the treasure. $$$")
        else:
            print("\nGame Over! You choose none of the doors because you were afraid.")
