MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_money = 0.0


def calc_change(client, price):
    change_value = client - price
    return round(change_value, 2)


def accept_coffe(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}. Money refounded.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def insert_coins():
    print("Please insert coins.")
    coins = int(input("How many quarters? ")) * 0.25
    coins += int(input("How many dimes? ")) * 0.1
    coins += int(input("How many nickles? ")) * 0.05
    coins += int(input("How many pennies? ")) * 0.01
    return coins


def report_print():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${machine_money}")


on = True

while on:
    i = input("What would you like? (espresso/latte/cappuccino):")
    if i == "off":
        print("Machine turned off.")
        on = False
    elif i == "report":
        report_print()
    else:
        coffe = MENU[i]
        client_coins_total = insert_coins()
        coffe_price = coffe["cost"]
        change = calc_change(client_coins_total, coffe_price)
        if change < 0:
            print("Sorry, that's not enough money. Coins refounded.")
            on = False
        else:
            print(f"Here is ${change} in change.")

        if accept_coffe(coffe["ingredients"]):
            machine_money += coffe["cost"]
            make_coffee(i, coffe["ingredients"])
