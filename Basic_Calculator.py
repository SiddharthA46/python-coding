# Problem Statement: Simple Calculator
# Objective:
# Your task is to build a simple calculator program that can perform basic arithmetic operations such as addition, subtraction,
# multiplication, and division.
while True:
    try:
        a = float(input('Enter the First number: '))

        break  # break out of the loop if input is successfully converted to float
    except ValueError:
        print('Please enter a valid number.')

while True:
    try:
        b = float(input('Enter the Second number: '))
        break  # break out of the loop if input is successfully converted to float
    except ValueError:
        print('Please enter a valid number.')

a = float(a)
b = float(b)

c = input('Select the operation: +, -, *, / : ')

if c == '+':
    print('The answer is:', a + b)
elif c == '-':
    print('The answer is:', a - b)
elif c == '/':
    if b == 0:
        print("Error: Division by zero")
    else:
        print('The answer is:', a / b)
elif c == '*':
    print('The answer is:', a * b)
else:
    print('Invalid operation selected.')
