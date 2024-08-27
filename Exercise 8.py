""" 
Exercise 8: Simple Calculator

"""

try:
    fir = int(input("Enter first number: "))
    amp = input("Enter an operator: ")
    sec = int(input("Enter second number: "))
    
    if amp == '*':
        ans = fir * sec
        print(f'The result is {ans}.')
    elif amp =='+':
        ans = fir + sec
        print(f'The result is {ans}.')
    elif amp =='-':
        ans = fir - sec
        print(f'The result is {ans}.')
    elif amp =='/':
        ans = fir / sec
        print(f'The result is {ans}.')
    else:
        print("Invalid Operator")

except ValueError:
    print("Error: Wrong Input.")