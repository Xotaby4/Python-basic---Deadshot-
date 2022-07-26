def decor(func):
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)
    return wrap


def decor(*decors_args, **decors_kwargs):
    def big_wrap(func):
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)
        return wrap
    return big_wrap

