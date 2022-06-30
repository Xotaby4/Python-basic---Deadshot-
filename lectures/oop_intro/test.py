class Animal:
    pass


class Dog(Animal):
    def __init__(self):
        self.color = 'brown'

    def say(self):
        print("Haw")

    def bring_coffee(self):
        print('bring coffee by dog')


class Cat(Animal):
    def __init__(self):
        self.n_paws = 4

    def say(self):
        print("Meayw")


class CatDog(Cat, Dog):
    def sing_song(self):
        print("This dream, this dream...")


cat_dog = CatDog()


print(type(cat_dog))
print(isinstance(cat_dog, int))
print(isinstance(cat_dog, CatDog))
print(isinstance(cat_dog, Cat))
print(isinstance(cat_dog, Dog))
print('-----')
print(issubclass(CatDog, Cat))
print(issubclass(CatDog, list))

# cat_dog.sing_song()
# cat_dog.say()
# cat_dog.bring_coffee()


# print(CatDog.mro())
