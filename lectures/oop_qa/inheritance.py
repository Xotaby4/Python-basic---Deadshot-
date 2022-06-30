class A:
    def method(self):
        print('A class method')


class B:
    def method(self):
        print('B class method')


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.method()

print(D.mro())