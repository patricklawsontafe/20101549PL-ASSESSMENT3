class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.sensors = sensors or []
        self.plates = plates or []
        self.capacity = capacity
        self.displays = displays or []

    def __str__(self):


        return f"Car park '{self.location}' contains {self.capacity} bays."
