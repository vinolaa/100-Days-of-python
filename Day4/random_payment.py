import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# USING LIST
number_people = len(names)
pay_person = random.randint(0, number_people - 1)
name_pay = names[pay_person]
print(f"{name_pay} is going to buy the meal today!")

# MOST EFFICIENT WAY
# name_pay = random.choice(names)
# print(name_pay)
