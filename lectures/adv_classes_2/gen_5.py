

def gen(num):
    v = yield 2
    w = yield v
    pass


generator = gen(10)
a = next(generator)

b = generator.send("a")
generator.throw(StopIteration)
c = generator.send("b")
pass
