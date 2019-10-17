import math

try:
    radius = int(input("Please enter the radius of the circle "))

    area = round(math.pi * radius**2 , 2)

    print("The area of your circle is", area)

except:
    print("Please enter a valid number")