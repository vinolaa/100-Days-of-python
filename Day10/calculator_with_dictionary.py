from Modulos.day10 import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def calc():
    print(logo)
    n1 = float(input("What's the first number? "))

    keep = True
    while keep:
        for s in operations:
            print(s)
        operational = input("Pick an operation from the list: ")
        n2 = float(input("What's the next number? "))
        operation = operations[operational]
        result = operation(n1, n2)
        print(f"{n1} {operational} {n2} = {result}")

        option = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
        if option == 'y':
            n1 = result
        else:
            keep = False
            calc()

calc()
