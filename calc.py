# Basic Calculator Program

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Prompt user for input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")