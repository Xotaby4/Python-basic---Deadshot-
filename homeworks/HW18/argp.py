import csv, json


class SomeUser:
    def __init__(self, fullname, age, location):
        self.fullname = fullname
        self.age = age
        self.location = location


class CustomSerializer:

    @staticmethod
    def normalize(user: SomeUser) -> dict:
        return {
            'name': user.fullname.split()[0],
            'surname': user.fullname.split()[1],
            'age': int(user.age),
            'coutnry': user.location.split()[0],
            'city': user.location.split()[1]
        }

    def serialize(self, user: SomeUser, format_: str):
        self.user = CustomSerializer.normalize(user)
        if format_.upper() == "CSV":
            self.obj2csv()
        elif format_.upper() == "JSON":
            self.obj2json()

    def obj2csv(self):
        with open('users.csv', 'w') as fc:
            writer = csv.DictWriter(fc, list(self.user.keys()), delimiter=';')
            writer.writeheader()
            writer.writerow(self.user)

    def obj2json(self):
        with open('users.json', 'w') as fj:
            json.dump(self.user, fj)


if __name__ == '__main__':
    denchyk = SomeUser('Denys Dalebiha', 31, 'Ukraina Kyiv')
    petya = SomeUser('Petro Motivator', 32, 'Ukraina Hlivyshche')
    serializer = CustomSerializer()
    serializer.serialize(denchyk, 'json')
    serializer.serialize(petya, 'csv')
