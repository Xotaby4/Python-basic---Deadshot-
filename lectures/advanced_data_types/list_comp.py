numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = []

for num in numbers:
    result = num * 2
    lst.append(result)

print(lst)


lst_comp = [num*2 for num in numbers]
print(lst_comp)

new_list = [x for x in numbers if x % 2 == 1]
print(new_list)

new_list_2 = [x**2 if x % 2 == 0 else x**3 for x in numbers]
print(new_list_2)