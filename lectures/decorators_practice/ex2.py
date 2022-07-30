

def decorator(flag):
    def big_wrap(func):
        def wrap(a, b):
            res = func(a, b)
            print(f"{a} + {b} = {res}")
            return res
        return wrap

    def big_wrap_1(func):
        def wrap(a, b):
            res = func(a, b)
            print(res)
            return res
        return wrap

    if flag:
        return big_wrap
    else:
        return big_wrap_1


class Execute:
    def __init__(self, model):
        self.model = model

    def __call__(self, func):
        def wrap(data):
            self.validate(data)
            return func(data)
        return wrap

    def validate(self, data):
        for model_field, model_settings in self.model.items():
            if data.get(model_field):
                pass


class Execute2(Execute):
    def validate(self, data):
        pass


data = {
    "id": 111,
    "name": "Misha"
}


@Execute(
    model={
        "id": {
            "required": True,
            "type": int
        },
        "name": {
            "required": True,
            "type": str
        },
        "age": {
            "required": False,
            "type": int

        }
    }
)
def my_func(data: dict):
    pass


my_func(data)

