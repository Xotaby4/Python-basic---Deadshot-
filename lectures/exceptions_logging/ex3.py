
def div(a, b):
    if b == 0:
        return 0

    try:
        c = a / b
    except ZeroDivisionError:
        c = 0
    else:
        print("ELSE")
    finally:
        print("FINALY")

    return c

# div(1, 0)
div(1, 1)

