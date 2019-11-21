
___author___ = "Jamie Neighbours"
___email___= "u1854720@unimail.hud.ac.uk"
___version___="3.0"


import re

only_speed = []
speed_list = []

still_reading = True
SPEED_LIMIT = 50
KMH_FACTOR = 1.609
vehicle_types = [0]*4


#Connverts any given integer to a percentage
def pc(value,number_of_items):
    percentage = str(round(((value / number_of_items) * 100), 2))
    percentage = percentage + "%"
    return percentage

#Converts to KM/H based on a factor of 1.609
def convert_to_kmh(speed):
    kmh = int(speed) * KMH_FACTOR
    kmh = str(round(kmh,2))
    kmh = kmh+"KPH"
    return kmh

#Calculates the number of speed violations using the array passed to it directly from the speed camera
def speed_violations():
    violations = 0

    for i in range(len(only_speed)):
        only_speed[i] = int(only_speed[i])
        if only_speed[i] > SPEED_LIMIT:
            violations = violations + 1
    return violations


#Takes any number of speed readings until the user types in "END"
#also checks to make sure some data has been entered
while still_reading == True:
    data_stream = (input("Enter next reading\n"))
    if re.match('^(H[\d]{2}|L[\d]{2}|C[\d]{2})$', data_stream) and (data_stream[1:] > "00"):
        speed_list.append(str(data_stream))
    elif len(speed_list) == 0 and data_stream == "END":
        print("No data provided")
        exit()
    elif data_stream == "END":
        still_reading = False
    else:
        print("Input invalid, try again!")

#Takes the data stream and slices the identifyer and converts to a list of integers
for x in speed_list:
    only_speed.append(int(x[1:]))

#Stores vehicle types for processing, index in array, 0 = heavy, 1 = light, 2 = car
for x in speed_list:
    if x[:1] == "H":
        vehicle_types[0] += 1
    elif x[:1] == "L":
        vehicle_types[1] += 1
    elif x[:1] == "C":
        vehicle_types[2] += 1

average_speed = sum(only_speed)/len(only_speed)

print(f"Number of vehicles: {len(speed_list)}")

print(f"Number of heavy goods: {vehicle_types[0]}({pc(vehicle_types[0],len(speed_list))})")

print(f"Number of light goods: {vehicle_types[1]}({pc(vehicle_types[1],len(speed_list))})")

print(f"Number of cars: {vehicle_types[2]}({pc(vehicle_types[2],len(speed_list))})")

print(f"The highest speed seen: {max(only_speed)}MPH ({convert_to_kmh(int(max(only_speed)))})")

print(f"The lowest speed seen: {min(only_speed)}MPH ({convert_to_kmh(min(only_speed))})")

print(f"The average speed seen: {round(average_speed, 1)}MPH ({convert_to_kmh(average_speed)})\n")

print(f"Speed limit violations: {speed_violations()}({pc(speed_violations(),len(only_speed))})")

