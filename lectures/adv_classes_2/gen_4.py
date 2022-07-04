

def gen(num):
    for i in range(num):
        print(f"HELLO!!! {i}")
        yield


def gen_2(num):
    for i in range(num):
        print(f"BY!!! {i}")
        yield


g1 = gen(10)
g2 = gen_2(5)

queue = [g1, g2]

while len(queue) > 0:
    cur_gen = queue.pop(0)
    try:
        next(cur_gen)
    except StopIteration:
        pass
    else:
        queue.append(cur_gen)

