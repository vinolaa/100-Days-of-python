print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

two_names = name1 + name2
two_names_s = two_names.lower()

letter_t = two_names_s.count("t")
letter_r = two_names_s.count("r")
letter_u = two_names_s.count("u")
letter_e = two_names_s.count("e")

true = letter_t + letter_r + letter_u + letter_e

letter_l = two_names_s.count("l")
letter_o = two_names_s.count("o")
letter_v = two_names_s.count("v")
letter_e = two_names_s.count("e")

love = letter_l + letter_o + letter_v + letter_e

total = str(true) + str(love)
total_int = int(total)

if total_int < 10 or total_int > 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int >= 40 and total_int <= 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}.")
