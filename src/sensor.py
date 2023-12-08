from abc import ABC, abstractmethod

import random

class Sensor(ABC):
    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id} || Active? {self.is_active}"
    
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)
    
    @abstractmethod
    def update_car_park(self, plate):
        pass



    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"A car entered the car park. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"A car exited the car park. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)