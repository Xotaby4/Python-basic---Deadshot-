class Box:
    pass


class Container(Box):
    def __init__(self, capacity):
        if capacity < 1:
            raise Exception('')
        else:
            self.capacity = capacity

    def __str__(self):
        return f'Container with values: {self.capacity}'

    def __repr__(self):
        return f'Container with values: {self.capacity}'

    # def setup_object(self, capacity):
    #     if capacity < 1:
    #         raise Exception('')
    #     else:
    #         self.capacity = capacity

    def some_method(self):
        print('abc')


box_1 = Container(5)
# box_1.setup_object(5)
print(box_1)
print(box_1.capacity)
box_1.some_method()


class Car(Container):
    pass
