

def func(a, b):
    print("START")
    try:
        c = a / b
    except ZeroDivisionError:
        c = 0
    print("FINAL")

    return c

func(1, 1)
print("----")
func(1, 0)
print("----")
func("1", 0)