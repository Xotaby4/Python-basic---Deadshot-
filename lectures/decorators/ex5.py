import uuid


def check_access(func):
    def wrap(self, value, user):
        if user in self.users:
            return func(self, value)
        else:
            raise Exception("NoAccess")
    return wrap


class Company:
    def __init__(self, name):
        self.users = []
        self.name = name

    @check_access
    def set_new_name(self, value):
        self.name = value

    @check_access
    def create_event(self):
        pass


class User:
    def __init__(self):
        self.id = uuid.uuid4()
        self.company = None


company = Company("My")
user = User()
# company.users.append(user)

company.set_new_name("MY2", user)
company.create_event(user)
pass

