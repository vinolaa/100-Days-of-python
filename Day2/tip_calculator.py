print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_bill += (total_bill * (percentage/100))
result_per_person = "{:.2f}".format(total_bill/people)
print(f"Each person should pay: ${result_per_person}")

