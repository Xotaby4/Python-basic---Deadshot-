class Vehicle:
    def __init__(self, color, size):
        self._color = color
        self.size = size

    def transport(self):
        print("Something is being transported")


class WheeledVehicle(Vehicle):
    def __init__(self, color, size, wheel_number):
        super().__init__(color, size)
        self.wheel_number = wheel_number

        self.__engine_volume = 2.5

    def get_gas_consuming(self, km):
        print(self._color)
        return km * self.__engine_volume


class SwimmingVehicle(Vehicle):
    def __init__(self, color, size, wheel_number):
        super().__init__(color, size)

    def get_gas_consuming(self, km):
        print(self._color)
        return km * self.__engine_volume



car = WheeledVehicle('white', 'large', 4)
car.transport()
print(car.get_gas_consuming(100))
print(car._color)
print(car._WheeledVehicle__engine_volume)
