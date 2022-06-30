class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100


class Bus(Vehicle):
    pass


bus_1 = Bus('bus', 100, 50)
bus_1.fare()
