# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(f"id(int_a) = {id(int_a)},\t id(str_b) = {id(str_b)}\n",
      f"id(set_c) = {id(set_c)},\t id(lst_d) = {id(lst_d)}\n",
      f"id(dict_e) = {id(dict_e)}\n")
#  id(int_a) = 9790688,	 id(str_b) = 139841784723632
#  id(set_c) = 139841784690496,	 id(lst_d) = 139841785076736
#  id(dict_e) = 139841785527488

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d += [4, 5]  # or lst_d.append(4); lst_d.append(5)
print(f"id(lst_d) = {id(lst_d)}\n")
# id(lst_d) = 139841785076736

# 3. Define the type of each object from step 1.
print(f"type(int_a) = {type(int_a)},\t type(str_b) = {type(str_b)}\n",
      f"type(set_c) = {type(set_c)},\t type(lst_d) = {type(lst_d)}\n",
      f"type(dict_e) = {type(dict_e)}\n")
#  type(int_a) = <class 'int'>,	 type(str_b) = <class 'str'>
#  type(set_c) = <class 'set'>,	 type(lst_d) = <class 'list'>
#  type(dict_e) = <class 'dict'>

# 4*. Check the type of the objects by using isinstance.
print(f"isinstance(int_a, int) = {isinstance(int_a, int)},\t "
      f"isinstance(str_b, str) = {isinstance(str_b, str)}\n",
      f"isinstance(set_c, set) = {isinstance(set_c, set)},\t i"
      f"isinstance(lst_d, list) = {isinstance(lst_d, list)}\n",
      f"isinstance(dict_e, dict) = {isinstance(dict_e, dict)}\n")
#  isinstance(int_a, int) = True,	 isinstance(str_b, str) = True
#  isinstance(set_c, set) = True,	 isinstance(lst_d, list) = True
#  isinstance(dict_e, dict) = True

'''String formatting:
Replace the placeholders with a value:
"Anna has ___ apples and ___ peaches."
'''
# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(3, 5))
# Anna has 3 apples and 5 peaches.

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(3, 5))
# Anna has 3 apples and 5 peaches.

# 7. By using keyword arguments into the curly braces.
print("Anna has {number_apples} apples and {number_peaches} "
      "peaches.".format(number_apples=3, number_peaches=5))
# Anna has 3 apples and 5 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {number_apples:5} apples and {number_peaches:3} "
      "peaches.".format(number_apples=3, number_peaches=5))
# Anna has     3 apples and   5 peaches.

# 9. With f-strings and variables
print(f"Anna has {5} apples and {3} peaches.")
# Anna has 3 apples and 5 peaches.

# 10. With % operator
print("Anna has %d apples and %s peaches." % (5, "no one"))
# Anna has 5 apples and no one peaches.

# 11*. With variable substitutions by name (hint: by using dict)
print("Anna has %(number_apples)d apples and %(number_peaches)s peaches." % {'number_apples': 5,
                                                                             'number_peaches': "no one"})
# Anna has 5 apples and no one peaches.

# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]
# 12. Convert (1) to list comprehension
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else
# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]
lst1 = []
for num in range(10):
    if num % 2 == 0:
        lst1.append(num // 2)
    else:
        lst1.append(num * 10)
print(lst1)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14. Convert (3) to dict comprehension.
# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.
# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}
d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
# (5)
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(dict_comprehension)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.
# (6)
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print(d)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}


''' Lambda: '''


# 18. Convert (7) to lambda function
# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y


print(foo(3, 5))
# 3
assert foo(3, 5) == 3, 'error in foo'

min2num = lambda x, y: x if x < y else y
print(min2num(3, 5))
# 3
assert min2num(3, 5) == 3, 'error in min2num'

# 19*. Convert (8) to regular function
# (8)
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(1, 2, 3))


# 2
def fo0(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(fo0(1, 2, 3))
# 2

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))
# [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda x, y: x + y, list_A, list_B)))
# [7, 9, 11]

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))
# [5, 1, 33, 15, 13, 55]

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda x: x < 0, range(-10, 10))))
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_2, list_1)))
# [2, 3, 5, 7]
