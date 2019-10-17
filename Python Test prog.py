import math


def circle_area_cal():
    try:
        radius = int(input("Please enter the radius of the circle "))

        area = round(math.pi * radius**2 , 2)

        print("The area of your circle is", area)
        calculate_again()

    except:
        print("Please enter a valid number")
        circle_area_cal()


def calculate_again():
    answer = input(str("Do you want to calculate another area? Y/N? ")).lower().strip()
    if answer[0] == "y":
        circle_area_cal()
    elif answer[0] == "n":
        print("Exiting program")
    else:
        print("Please enter a valid input!")
        calculate_again()

circle_area_cal()