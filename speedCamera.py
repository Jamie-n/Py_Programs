
import re

only_speed = []
speed_list = []
still_reading = True
SPEED_LIMIT = 50
KMH_FACTOR = 1.609
vehicle_types = [0]*4

def convert_to_percentage(value,number_of_items):
    percentage = str(round(((value / number_of_items) * 100), 2))
    percentage = percentage + "%"
    return percentage


def convert_to_kmh(speed):
    kmh = str(round(speed * KMH_FACTOR, 2))
    kmh = kmh+"KPH"
    return kmh



#Takes any number of speed readings until the user types in "END"
while still_reading == True:
    data_stream = (input("Enter next reading\n"))
    if re.match('^(H)\d\d|(L)\d\d|(C)\d\d$', data_stream):
        speed_list.append(str(data_stream))
    elif data_stream == "END":
        still_reading = False
    elif len(speed_list) == 0 and data_stream == "END":
        print("No data provided")
        exit()
    else:
        print("Input invalid, try again!")


def speed_violations(camera_speeds):

    speed_violations = 0
    for x in speed_list:
       only_speed.append(x[1:])

    for i in range(len(only_speed)):
        only_speed[i] = int(only_speed[i])
        if only_speed[i] > SPEED_LIMIT:
            speed_violations = speed_violations + 1
    return speed_violations

# Stores vehicle types for processing, index in array, 0 = heavy, 1 = light, 2 = car, 3 = unknown

for x in speed_list:
    if x[:1] == "H":
        vehicle_types[0] += 1
    elif x[:1] == "L":
        vehicle_types[1] += 1
    elif x[:1] == "C":
        vehicle_types[2] += 1


print(f"Number of vehicles: {len(speed_list)}")
print(f"Number of heavy goods: {vehicle_types[0]}({convert_to_percentage(vehicle_types[0],len(speed_list))})")
print(f"Number of light goods: {vehicle_types[1]}({convert_to_percentage(vehicle_types[1],len(speed_list))})")
print(f"Number of cars: {vehicle_types[2]}({convert_to_percentage(vehicle_types[2],len(speed_list))})")


print(f"The highest speed seen: {max(only_speed)}MPH ({convert_to_kmh(max(only_speed))})")
print(f"The lowest speed seen: {min(only_speed)}MPH ({convert_to_kmh(min(only_speed))})")

average_speed = (sum(only_speed)/(len(only_speed)))
print(f"The average speed seen: {round(average_speed, 1)}MPH ({convert_to_kmh(average_speed)})\n")

print(f"Speed limit violations: {speed_violations}({convert_to_percentage(speed_violations,len(only_speed))})")