x = 5
print(type(x))
print(id(x))


def foo(x):
    return x * x


print(type(foo))
print(id(foo))

lst = [1, 2, 3]


def modify_list(lst, fn):
    for index, value in enumerate(lst):
        lst[index] = fn(value)


modify_list(lst, foo)
print(lst)

foo_1 = lambda x, y, z: x * y * z
print(type(foo_1))

foo_1 = lambda fn, y, z: fn(y) * y * z



numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_fn(x):
    if x % 2 == 0:
        return True
    return False

print(list(filter(even_fn, numbers)))

print(list(filter(lambda x: x % 2 == 0, numbers)))


def multiple_2(x):
    return x * 2

print(list(map(multiple_2, numbers)))

print(list(map(lambda x: x * 2, numbers)))


lst = [5, 7, 1, 3]

print(sorted(lst))

d = {'Alex': 30, 'Bob': 15, 'David': 7}
l = ['Alex', 'Bob', 'David']
l.sort(key=lambda x: d[x])
print(l)
