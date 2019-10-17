
def sweetProgram():
    try:

        pupilsInClass = int(input("How many students are there in the class?"))
        sweetsInBag = int(input("How many sweets are there in the bag?"))

        sweetsPerStudent = divmod(sweetsInBag, pupilsInClass)

        print("There are sweets",sweetsPerStudent[0],"per student, of these",sweetsPerStudent[1],"are leftover")

    except:
        print("Please enter a valid number!")
        sweetProgram()

sweetProgram()