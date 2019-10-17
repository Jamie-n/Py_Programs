

def celciusToFarenheight():
   tempInCelcius = float(input("What is the temprature in celcius that you would like to convert?"))
   tempInFarenheight = round((tempInCelcius * 9 / 5) + 32)
   print("Your temprature in farenheight is" ,tempInFarenheight,"F")


def farenheeightToCelcius():
    tempInFarenehight = float(input("What is the temprature in farenheight that you would like to convert?"))
    tempInCelcius = round((tempInFarenehight -32) /9 * 5)
    print("Your temprature in celcius is",tempInCelcius,"C")

def askUserInput():
    likeToCovert = input("Would you like to convert from farenheight to celcius y/n?")

    if likeToCovert == "y":
        farenheeightToCelcius()
    elif likeToCovert == "n":
        celciusToFarenheight()
    else:
        print("Please enter either y or n")
        askUserInput()

askUserInput()


