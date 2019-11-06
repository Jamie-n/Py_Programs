



NUMBER_OF_SWEETS = 5
POUND_MULTIPLY = 100

price_of_sweets = []
x = 0

def parse_prices(price):
    if price[0] == "£":
        price = price.strip().lstrip("£")
        price = int(price) * 100
    else:
        price = price.strip("p")
    return int(price)

def convert_to_currency(value):

    if value > 100:
        value = value / 100
        value = "£" + str(value)
    else:
        value = str(value) +"p"

    return value


while x < NUMBER_OF_SWEETS:
    sweet_price = input("Please enter the price of sweet " + str(x+1) +"?\n")

    if sweet_price.startswith("£") or sweet_price.endswith("p"):
        price_of_sweets.append(parse_prices(sweet_price))
        print(price_of_sweets)
        x = x + 1
        print(x)
    else:
        print("Please input a number followed by a currency symbol")





total_price = sum(price_of_sweets)



print(f"The total price is {convert_to_currency(total_price)}")

average_price = total_price / NUMBER_OF_SWEETS

print(f"The average price is {convert_to_currency(average_price)}")

highest_price = max(price_of_sweets)

print(f"The highest sweet price is {convert_to_currency(highest_price)}")

lowest_price = min(price_of_sweets)

print(f"The lowest price is {convert_to_currency(lowest_price)}")




