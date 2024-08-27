"""
Exercise 7: Temperature Check

"""

cels = int(input("Enter the temperature in Celsius: "))
if cels < 10:
    print("It is Cold.")
elif cels <= 25:
    print("It is Warm.")
elif cels > 25:
    print("It is Hot.")