
'''
Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

'''
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation in ['+', '-', '*', '/']:
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        if y != 0:
            result = x / y
        else:
            result = "Error: Division by zero is not allowed."
    
    print(f"{x} {operation} {y} = {result}")