list_1 = [1, 2, 3, 4, 5]
ind = 0

# while True:
#     if ind >= len(list_1):
#         break
#     print(list_1[ind])
#     ind += 1


iter_list = iter(list_1)
while True:
    try:
        print(next(iter_list))
    except StopIteration:
        break

print("END")