import unittest
import random

from sensor import EntrySensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EntrySensor(1, CarPark(), True)
        self.car_park = CarPark()

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.sensor.car_park, CarPark)

    def test_update_car_park(self):
        plate = format(random.randint(0, 999), "03d")
        self.car_park.add_car(plate)
        self.assertEqual(self.car_park.plates[0], plate)

