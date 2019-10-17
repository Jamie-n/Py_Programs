

def calculate_area():
    try:
        rectangle_Length = float(input("Please enter the length of the rectangle "))
        rectangle_Width = float(input("Please enter the width of the rectangle "))
        rectangle_Area = rectangle_Length * rectangle_Width
        print(rectangle_Area)

    except:
        print("Please enter a positive number!")
        calculate_area()

calculate_area()


