
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.parent = None
        self.child = []

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def set_parent(self, user):
        self.parent = user
        user.child.append(self)
