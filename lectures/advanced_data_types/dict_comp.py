lst = [("number_a", "1"),
       ("number_b", "2")]

dictionary = {}
for tup in lst:

    key = tup[0]
    value = tup[1]

    dictionary[key] = value

print(dictionary)
print(dictionary['number_a'])
print(dictionary['number_b'])
# {'a': '1', 'c': '1'}

dict_comp = {k: v for k, v in lst}
print(dict_comp)
print(dict_comp['number_a'])
print(dict_comp['number_b'])
# # {'a': 'b', 'c': 'd'}

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dc_with_if = {x: x**3 for x in numbers if x % 2 == 0}
print(dc_with_if)

dc_with_elif = {x: x**3 if x % 2 == 0 else x for x in range(10)}
print(dc_with_elif)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
