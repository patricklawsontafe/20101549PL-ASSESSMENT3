from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

import time
import random

car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")

entry_sensor = EntrySensor(1, car_park, True)
exit_sensor = ExitSensor(2, car_park, True)

display = Display(1, car_park, "Welcome to Moondalup", True)

print(display, "\n")
for i in range(10):
    new_plate = format(random.randint(0, 999), "03d")
    entry_sensor.update_car_park(new_plate)

    time.sleep(1)

time.sleep(2)
for i in range(2):
    new_plate = random.choice(car_park.plates)
    exit_sensor.update_car_park(new_plate)

    time.sleep(1)