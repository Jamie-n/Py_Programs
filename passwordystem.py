



passes_match = False
PASS_UPPER_BOUND = 12
PASS_LOWER_BOUND = 6



def check_length(password):

    if len(password) >= PASS_LOWER_BOUND or password <= PASS_UPPER_BOUND:
        return True


while passes_match == False:
    password_1 = input("Please enter your password\n")
    password_2 = input("Please re-enter your password\n")


    if password_1 == password_2 and check_length(password_1):
        passes_match = True
        print("Password Changed!")
    else:
        print("Passwords did not match please try again")