"""
Exercise 3: Complex Nested Conditions - Employee Bonus Calculation

"""

year = int(input("Enter years of service: "))
rate = input("Enter performance rating (Excellent, Good, Average): ")
sala = int(input("Enter salary: "))
total = float(0)

if year > 10:
    if rate in 'excellentExcellentEXCELLENT':
        total = sala * 0.2
        print("The bonus is", total)
    elif rate in 'goodGoodGOOD':
        total = sala * 0.18
        print("The bonus is", total)
    elif rate in 'averageAverageAVERAGE':
        total = sala * 0.15
        print("The bonus is", total)
        
elif year <= 10:
    if rate in 'excellentExcellentEXCELLENT':
        total = sala * 0.15
        print("The bonus is", total)
    elif rate in 'goodGoodGOOD':
        total = sala * 0.13
        print("The bonus is", total)
    elif rate in 'averageAverageAVERAGE':
        total = sala * 0.1
        print("The bonus is", total)

elif year <  5:
    if rate in 'excellentExcellentEXCELLENT':
        total = sala * 0.10
        print("The bonus is", total)
    elif rate in 'goodGoodGOOD':
        total = sala * 0.08
        print("The bonus is", total)
    elif rate in 'averageAverageAVERAGE':
        total = sala * 0.05
        print("The bonus is", total)