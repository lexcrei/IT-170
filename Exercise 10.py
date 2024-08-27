"""
Exercise 10: Nested Ternary Operations - Discount Calculator

"""
import math

bill = int(input("Enter the purchase amount: "))
mem = input("Are you a member (yes/no)?: ")
if bill >= 10000:
    if mem in 'yesYesYES':
        total = bill * 0.22
        amt = bill - total
        print(f"The final amount after discount is {amt}")
    else:
        total = bill * 0.2
        amt = bill - total
        print(f"The final amount after discount is {amt}")
        
elif bill < 10000:
    if mem in 'yesYesYES':
        total = bill * 0.12
        amt = bill - total
        print(f"The final amount after discount is {amt}")
    else:
        total = bill * 0.1
        amt = bill - total
        print(f"The final amount after discount is {amt}")
    
elif bill < 5000:
    if mem in 'yesYesYES':
        total = bill * 0.07
        amt = bill - total
        print(f"The final amount after discount is {amt}")
    else:
        total = bill * 0.05
        amt = bill - total
        print(f"The final amount after discount is {amt}")