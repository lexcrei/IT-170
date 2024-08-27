try:
    circles = input("Enter the lengths of the three sides of the triangle: ")
    if circles[1] == circles[2] == circles[0]:
        print("The triangle is valid and it is equilateral")
    elif circles[0] == circles[1] or circles[1] == circles[2] or circles[2] == circles[0]:
        print("The triangle is valid and it is isoceles")
    elif circles[0] != circles[1] != circles[2] != circles[0]:
        print("The triangle is valid and it is scalene")
    else:
        print("The triangle is invalid due to unknown input")

except ValueError:
    print("Error: What did you do??")
except IndexError:
    print("Error: Don't put spaces on the text please.")