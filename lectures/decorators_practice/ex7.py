

def func(*args, **kwargs):
    args = list(args)
    print(args)
    # print(kwargs)

func()
func(1, 2, 3, 4, 5, a=6, b=4)
func(1)