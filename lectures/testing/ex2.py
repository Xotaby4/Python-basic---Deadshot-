
def div(a, b):
    return a / b

#
# if div(1, 1) == 2:
#     print("SUCCESS")
# else:
#     raise Exception("FAIL")
#
# if div(4, 2) == 2:
#     print("SUCCESS")
# else:
#     raise Exception("FAIL")


res = div(1, 1)
assert res == 2, f"{res} != 2"
