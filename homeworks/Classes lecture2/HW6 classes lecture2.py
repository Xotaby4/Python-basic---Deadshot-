#1.
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self, name, diagonal, pzu, capacity):
        self.name = name
        self.diagonal = diagonal
        self.pzu = pzu
        self.battery = Battery(capacity)
class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.bat_type = "Li-ion"
hp = Laptop("HP", 15, 1024, 65)
print(hp.battery.capacity)
# 65

#2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, brand, *string):
        self.brand = brand
        self.string =[x for x in string]
class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, number, st_type, tension):
        self.number = number
        self.st_type = st_type
        self.tension = tension

string1 = GuitarString(0, "black nylon", "Normal Tension")
string2 = GuitarString(1, "clear nylon", "High Tension")
string3 = GuitarString(2, "bronze wound", "High Tension")
string4 = GuitarString(3, "clear nylon", "High Tension")
string5 = GuitarString(4, "bronze wound", "High Tension")
string6 = GuitarString(5, "bronze wound", "High Tension")
guitar = Guitar("homemade", string1, string2, string3, string4, string5, string6)
print(guitar.string[5].st_type)
# bronze wound
del guitar
print(string6.st_type)
# bronze wound

#3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should be static
    """
    @staticmethod
    def add_nums(n1, n2, n3):
        return n1 + n2 + n3
print(Calc.add_nums(1, 2, 3))
# 6

#4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
    def __init__(self, *ingredients):
        self.ingredients = [x for x in ingredients]
    def __str__(self):
        return f"ingredients of Pasta is {self.ingredients}"

    @staticmethod
    def carbonara():
        return Pasta(['forcemeat', 'tomatoes'])
    @staticmethod
    def bolognaise():
        return Pasta(['bacon', 'parmesan', 'eggs'])

pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()
pasta_3 = Pasta.carbonara()
print(f"{pasta_1},\n{pasta_2}, \n{pasta_3}")
# ingredients of Pasta is [['tomato', 'cucumber']],
# ingredients of Pasta is [['bacon', 'parmesan', 'eggs']],
# ingredients of Pasta is [['forcemeat', 'tomatoes']]


#5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    def __init__(self, max_visitors_num, visitors_count):
        # self.max_visitors_num = self.__setattr__("max_visitors_num", max_visitors_num)
        # self.visitors_count = self.__setattr__("visitors_count", visitors_count)
        super(Concert, self).__setattr__("max_visitors_num", max_visitors_num)
        super(Concert, self).__setattr__("visitors_count", visitors_count)
    def __setstate__(self, name, value):
        if name == "visitors_count" and value > self.max_visitors_num:
            value = self.max_visitors_num
            super(Concert, self).__setattr__(name, self.max_visitors_num)
        else:
            super(Concert, self).__setattr__(name, value)
concert = Concert(50, 60)
# #concert.visitors_count = 10
print(f"concert.visitors_count = {concert.visitors_count}")
# concert.visitors_count = 60
# поки не знаю як реалізувати.
#6.
import dataclasses
@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
    birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int
AddressBook = AddressBookDataClass (0, "Denys", "+102356879454", "Clayton St, San Francisco, CA 94114, USA",
                                    "SF94114@gmail.com", "3/14/15", 7)
print(AddressBook)
# AddressBookDataClass(key=0, name='Denys', phone_number='+102356879454',\
# address='Clayton St, San Francisco, CA 94114, USA', email='SF94114@gmail.com', birthday='3/14/15', age=7)

#7. Create the same class (6) but using NamedTuple
from collections import namedtuple
AddressBookNamedTuple = namedtuple("AddressBookNamedTuple", ["key", "name", "phone_number",
                                    "address", "email", "birthday", "age"])
AddressBookNT = AddressBookNamedTuple (0, "Denys", "+102356879454", "Clayton St, San Francisco, CA 94114, USA",
                                    "SF94114@gmail.com", "3/14/15", 7)
print(AddressBookNT)
# AddressBookNamedTuple(key=0, name='Denys', phone_number='+102356879454', \
# address='Clayton St, San Francisco, CA 94114, USA', email='SF94114@gmail.com', birthday='3/14/15', age=7)

#8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='',
    email='', birthday= '', age='')
    """
    def __init__(self, key='', name='', phone_number='', address='', email='', birthday= '', age=''):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
    def __str__(self):
        return f"AddressBook(key='{self.key}', name='{self.name}', phone_number='{self.phone_number}', " \
               f"address='{self.address}', email='{self.email}', birthday= '{self.birthday}', age='{self.age}')"
AddressBookCl = AddressBook(0, "Denys", "+102356879454", "Clayton St, San Francisco, CA 94114, USA",
                            "SF94114@gmail.com", "3/14/15", 7)
print(AddressBookCl)
# AddressBook(key='0', name='Denys', phone_number='+102356879454', address='Clayton St, San Francisco, CA 94114, USA',\
# email='SF94114@gmail.com', birthday= '3/14/15', age='7')

#9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"
Person.age = 50
john = Person()
print(john.age)

#10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name
setattr(Student, "email", "byimoskalya@ukr.net")
student_email = getattr(Student, "email")
print(student_email)
# byimoskalya@ukr.net

#11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature = 0):
        self._temperature = temperature
    @property
    def temperature(self):
        return f"{self._temperature * 1.8 + 32}F"

# create an object
classroom_temperature = Celsius(27)
print(classroom_temperature.temperature)
#80.6F