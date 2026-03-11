num1=int(input("Enter the num1 value:"))
num2=int(input("Enter the num2 value:"))
operation = input("Enter operation (+, -, *, /): ")

def calculator(operation, num1, num2):
    match operation:
        case '+':
            return num1 + num2
        case '-': 
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            # Basic error handling
            if num2 == 0:
                return "Error! Division by zero."
            return num1 / num2
        case _:
            return "Invalid operation"

result = calculator(operation, num1, num2)

print("Result:", result)