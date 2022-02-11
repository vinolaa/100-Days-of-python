print("Welcome to the playground.")
height = int(input("What is your height in cm? "))

if height >= 120:
    bill = 0
    age = int(input("What is your age? "))
    if age < 12:
        bill = 3
        print("Ticket value for child: $3.")
    elif age <= 18:
        bill = 10
        print("Ticket value for youth: $10")
    else:
        bill = 15
        print("Ticket value for adult: $15")

    want_photos = input("Do you want photos? Type [Y] for YES or [N] for NO. ")
    if want_photos == "Y":
        bill += 5

    print(f"The total bill is ${bill}.")
else:
    print("Sorry, you do not have the necessary height.")
