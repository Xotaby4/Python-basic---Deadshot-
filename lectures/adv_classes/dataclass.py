import dataclasses


@dataclasses.dataclass(frozen=True)
class User:
    id: int
    name: str
    age: int


user_1 = User(1, "Misha", 12)
pass