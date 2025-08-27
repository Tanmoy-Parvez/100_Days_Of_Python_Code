from art import logo


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

print(logo)

first_number = float(input("What's the first number?: "))

should_continue = True

while should_continue:

    for key in operations:
        print(key)

    operator = input("Pick an operation: ")

    next_number = float(input("What's the next number?: "))

    result = operations[operator](first_number, next_number)
    print(f"{first_number} {operator} {next_number} = {result}")

    choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start new calculation: ")

    if choice == "y":
        first_number = result
    else:
        print("\n" * 20)
        print(logo)
        first_number = float(input("What's the first number?: "))