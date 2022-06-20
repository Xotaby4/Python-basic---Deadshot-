# Невизначений тип даних
# immutable
a = None # null
print(type(a))

# boolean - логічні типи даних
# immutable
b = True # 1
c = False # 0
print(type(c))

# числа
# immutable
d = 5 # int
e = 5.5 # float
f = 5e5 # complex (5+5i)

# string - рядки
# immutable
g = 'strings'
print(type(g))

# binary - бінарні типи даних
# mutable
h = b'strings'
print(type(h))

# set - множини
# mutable
i = {1, 2, 3, 4}
i_1 = frozenset(i)

# dict словники
# mutable
j = {"type": "hello"}

# list - списки
# mutable
k = [1, 2, '3', 4.2]

# tuple - незмінні списки
# immutable
l = (1, 2, '3', 4.2)


# lucky_number = 7
#
# import keyword
# print(f"Python keywords: {keyword.kwlist}")
#
# print(keyword.iskeyword("lucky_number"))
# print(keyword.iskeyword("try"))

w = 'string'
print(w)
print(id(w))
w = w + ' string'
print(w)
print(id(w))

o = [1, 2]
print(o)
print(id(o))
o.append(3)
print(o)
print(id(o))

u = 1
print(str(u))
