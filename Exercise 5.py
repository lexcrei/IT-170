"""
Exercise 5: Simple Interest Calculation
"""

prin = int(input("Enter Principal Amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time period in years: "))

inter = rate * 0.01
rest = prin * time * inter
total = int(rest)
if rate > 10:
    print(f"The simple interest is {total}. Warning: High interest rate.")
else:
    print(f"The simple interest is {total}.")