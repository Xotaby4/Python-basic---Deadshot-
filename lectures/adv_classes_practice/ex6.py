

def cour():
    i = 1
    finish = None
    while True:
        name = yield finish
        finish = f"{name} {i}"
        i += 1


gen = cour()
next(gen)
w = gen.send(100)
e = gen.send(150)


