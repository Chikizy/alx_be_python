num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operand = input("Choose the operation (+, -, *, /):")

match operand:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("incorrect operator")
if operand != "/" and num2 != 0:
    print(f"The result is {result}")