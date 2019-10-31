


NUMBER_OF_SWEETS = 5
POUND_MULTIPLY = 100

price_of_sweets = []

def parse_Prices(sweet_price):

    for i in sweet_price:
        if sweet_price[i][-1].lower() == "p":
            sweet_price = sweet_price[:-1]
        elif sweet_price[i][0] == "£":
            sweet_price = sweet_price[1:]

    print(sweet_price)

for x in range(0,NUMBER_OF_SWEETS):

    sweet_price = input("Please enter the price of sweet " + str(x+1) +"?\n")
    price_of_sweets.append(sweet_price)


parse_Prices(price_of_sweets)






print (price_of_sweets)