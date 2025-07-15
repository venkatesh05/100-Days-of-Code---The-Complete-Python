def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    should_continue = True
    number1 = float(input("What is the First number : "))

    while should_continue:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an Operation : ")
        number2 = float(input("What is the second number : "))
        answer = operations[operation_symbol](number1,number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation : ")

        if choice == "y":
            number1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()