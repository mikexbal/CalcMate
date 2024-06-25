def calculator():
    logo = """
     _____________________
    |  _________________  |
    | | CalcMate.       | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """

    print(logo)
    print("Welcome to CalcMate! Solving all of your simple math troubles.\n")

    #Mathematical Operations
    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1 * num2
    def divide(num1, num2):
        return num1 / num2

    #Operation Symbols
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    #Ask user for input
    num1 = int(input("Enter you first number: "))
    for opSymbol in operations:
        print(opSymbol)
    op = input("Select your operation: ")
    num2 = int(input("Enter you second number: "))

    #Calculate and solve!
    calc = operations[op]
    solution = calc(num1, num2)
    print(f"{num1} {op} {num2} = {solution}")

calculator()