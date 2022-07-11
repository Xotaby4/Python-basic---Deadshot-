def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass:
    pass

@singleton
class MyClass2:
    pass

obj = MyClass()
obj_2 = MyClass2()
obj_3 = MyClass()
pass