
class List:
    def __init__(self):
        self.list = []
        self.iterator = MyIter()

    def func(self):
        pass

    def __iter__(self):
        return self.iterator

    def __next__(self):
        self.index += 1
        return self.list[self.index]


class MyRange:
    def __init__(self, start_index, finish_index, step=1):
        self.start_index = start_index
        self.finish_index = finish_index
        self.step = step
        self.current_index = start_index - step

    def __iter__(self):
        return self

    def calc_next(self):
        return

    def __next__(self):
        self.current_index += self.step
        self.calc_next()
        if self.current_index >= self.finish_index:
            raise StopIteration
        return self.current_index


my_iter = MyRange(1, 10)

next(my_iter)

for i in MyRange(1, 20, 2):
    print(i)