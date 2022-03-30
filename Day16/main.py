from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        print("Machine turned off.")
        machine_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        sufficient = coffe_maker.is_resource_sufficient(drink)
        if sufficient:
            money_machine.make_payment(drink.cost)
            coffe_maker.make_coffee(drink)
