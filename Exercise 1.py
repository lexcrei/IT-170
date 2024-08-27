# Exercise 1: Grade Calculator
try:
    grade = int(input("Enter your score: "))
    if grade < 60:
        print("Your grade is F.")
    elif grade <= 69: # haha funny number
        print("Your grade is D.")
    elif grade <= 79:
        print("Your grade is C.")
    elif grade <= 89:
        print("Your grade is B.")
    else:
        print("Your grade is A.")
except ValueError:
    print("Invalid Input.")