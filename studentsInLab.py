

try:

    students = int(input("How many students are in the class?\n"))
    space_in_lab = int(input("How many computers are there per lab?\n"))


    if str(students).isdigit() and str(space_in_lab).isdigit():

        labs_needed = divmod(students, space_in_lab)

        if labs_needed[1] == 0:
            num_of_labs = labs_needed[0] + 1
            print(f"You will need exactly {num_of_labs} lab")
        elif labs_needed[1] > 0:
            num_of_labs = labs_needed[0] + 1
            print(f"You will need exactly {num_of_labs} labs")
        else:
            num_of_labs = labs_needed[0]
            print(f"You will need exactly {num_of_labs} labs")

except:
    print("Please enter a number!\n")





