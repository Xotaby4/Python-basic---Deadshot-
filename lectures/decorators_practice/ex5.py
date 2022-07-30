
def courutine(func):
    def wrap(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrap


@courutine
def generator():
    b = "Hello"
    a = yield b
    print(a)

gen = generator()
# next(gen)
gen.send("ALLLO")