# 1. Create a class Vehicle with Attributes: name, max_speed,
#    and total_capacity. Method: fare. It should calculate the price of the trip.
#    Formula: total_capacity * 100. Example, total_capacity = 50 => fare = 5000
class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def far(self):
        return self.total_capacity * 100
    def __str__(self):
        return f"{self.name} max.speed {self.max_speed} total capacity {self.total_capacity}"
    def __bool__(self):
        return True if self.max_speed > 90 else False

# 2. Create classes Bus and Car that inherit Vehicle.

class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    def far(self):
        return self.total_capacity * 110

    def set_used_capacity(self, used_capacity):
        if used_capacity > self.total_capacity:
            raise Exception(f"Error. The entered number is greater than the maximum allowable value. Enter a number less than or equal to {self.total_capacity}")
        else:
            self.user_capacity = user_capacity
    def __len__(self):
        return self.total_capacity//2*3

class Car(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)


# 3. Create 3 car objects and 2 bus objects
audi = Car("Audi", 320, 4)
mersedes = Car("Mersedes", 290, 5)
bmw = Car("BMW", 350, 5)
iveco = Bus("Iveco", 132, 18)
bohdan = Bus("Bohdan", 97, 50)

# 4. Check: if car_1 is instance of Car.
#    if car_2 is instance of Vehicle.
#    if bus_1 is instance of Car.
#    if bus_1 is instance of Vehicle.
print(f"audi is instance of Car - {isinstance(audi, Car)}")
# audi is instance of Car - True
print(f"mersedes  is instance of Vehicle - {isinstance(mersedes, Vehicle)}")
# mersedes  is instance of Vehicle - True
print(f"iveco is instance of Car - {isinstance(iveco, Car)}")
# iveco is instance of Car - False
print(f"iveco  is instance of Vehicle - {isinstance(iveco, Vehicle)}")
# iveco  is instance of Vehicle - True

# 5. Override fare method for Bus class.
#    Here we need to add an extra 10% to the fare.
#    Formula: total_fare + 10% of total_fare. Example, fare = 50 => total_fare = 5500
print(f"bohdan total capacity is {bohdan.total_capacity}, total fare {bohdan.far()}")
# bohdan total capacity is 50, total fare 5500

# 6. Add used_capacity attribute for Bus. It means how many people are on the bus.
#    If used_capacity > total_capacity raise an error.
iveco.set_used_capacity(20)
#Error. The entered number is greater than the maximum allowable value. Enter a number less than or equal to 18

# 7. Write a magic method to Bus that would be triggered when len() function is called.
#    To figure out what magic method you should implement, take a look at the full list of magic methods:
#    https://www.tutorialsteacher.com/python/magic-methods-in-python. Play around with other dunder methods
print (f"len of bohdan = {len(bohdan)}")
#len of bohdan = 75
print(audi)
#Audi max.speed 320 total capacity 4
print(bool(bmw))
#True

# 8. Create class Engine with attribute volume and method get_volume() that will return volume.
# 9. Inherit Engine by Car class.
class Engine(Car):
    __volume = 100
    def get_volume(self):
        return self.__volume
#print (f"Engine volue {Engine.__volume}")
#AttributeError: type object 'Engine' has no attribute '__volume'
print (f"Engine volue {Engine.get_volume(Engine)}")
#Engine volue 100

# 10. Check what is inheritance order of the Car class.
print(f"Engine is inherit of Car - {issubclass(Engine, Car)}")
#Engine is inherit of Car - True
print(Car.mro())
#[<class '__main__.Car'>, <class '__main__.Vehicle'>, <class 'object'>]
