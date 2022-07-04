
def func():
    print("step1")
    return
    print("step 2")

#
# func()
# func()


def func_generator(index):
    print("step1")
    index += 1
    yield index
    print("step 2")
    index += 2
    yield index


gen = func_generator(2)
a = next(gen)
b = next(gen)
print(a, b)
next(gen)

