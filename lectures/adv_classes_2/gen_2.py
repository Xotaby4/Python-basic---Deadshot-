
def my_range(start_index, finish_index, step=1):
    current_index = start_index - step
    while True:
        current_index += step
        if current_index >= finish_index:
            return
        yield current_index


for i in my_range(2, 25, 3):
    print(i)


generator = (i for i in range(10))

def gen_2():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7

