import time
import logging

logging.basicConfig(level=logging.INFO)


def decorator_timer(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(t2 - t1)
        return res
    return wrap


def decorator_logger(func):
    def wrap(*args, **kwargs):
        logging.info(f"start run {func.__name__}")
        res = func(*args, **kwargs)
        logging.info(f"finish run {func.__name__}")
        return res
    return wrap


@decorator_timer
@decorator_logger
def func():
    time.sleep(1)


@decorator_timer
@decorator_logger
def func_2():
    time.sleep(2)


func()
func_2()