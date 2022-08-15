# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
class FibonacciNumbers:
    def __init__(self, number):
        self.number = number
        self.f_1 = 1
        self.f_2 = 1
        self.f: int
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        elif self.counter < 2:
            self.counter += 1
            return 1
        else:
            self.counter += 1
            self.f = self.f_2 + self.f_1
            self.f_2, self.f_1 = self.f_1, self.f
            return self.f


for i in FibonacciNumbers(10):
    print(i, end=" ")


# 1 1 2 3 5 8 13 21 34 55

# 2. Implement generator for Fibonacci numbers
def fibonacci_generator(number):
    f_1, f_2 = 1, 1
    for i in range(number):
        yield f_1
        f_1, f_2 = f_2, f_1 + f_2


print("\n")
for i in fibonacci_generator(11):
    print(i, end=" ")


# 1 1 2 3 5 8 13 21 34 55 89


# 3. Write generator expression that returns square numbers of integers from 0 to 10

def quadro_gen(n):
    for i in range(1, n+1):
        yield i ** 2


q = quadro_gen(10)
print("\n")
for i in range(10):
    print(next(q), end=" ")


# 1 4 9 16 25 36 49 64 81 100

# 4.Implement coroutine for accumulation arithmetic mean

def accumulation_mean():
    counter = 0
    sum_ = 0
    counter += 1
    sum_ += yield sum_
    while True:
        sum_ += yield sum_ / counter
        counter += 1


acc_mean = accumulation_mean()
print("\n")
next(acc_mean)
print(acc_mean.send(2))  # 2.0
print(acc_mean.send(8))  # 5.0
print(acc_mean.send(2))  # 4.0
print(acc_mean.send(4))  # 4.0
am = accumulation_mean()
next(am)
print("\n")

for i in FibonacciNumbers(10):
    print(round(am.send(i),2), end=" ")
# 1.0 1.0 1.33 1.75 2.4 3.33 4.71 6.75 9.78 14.3
