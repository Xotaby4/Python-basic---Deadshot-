""""""

""" Task 1 
написати декоратор exception_wrapper - його задача подавити всі ексепшини які можуть згенеруватись в функції, і видати якийсь прінт
@exception_wrapper
def some_func(*args, **kwargs):
    pass
    
Приклад використання якщо в some_func згенеровано ексепшн
>>> some_func()
Internal Error

* можна додатково зробити конкретні прінти для певних ексепшинів
наприклад функція генерує NoAccess
>>> some_func()
You hasn't access

"""

""" Task 2
Написати декоратор expect, його завдання перевірити на відповідність певній моделі, аргумент що передається в функцію

Приклад
@expect({
    "id": {
        "type": int,
        "required": True,
    },
    "name": {
        "type": str,
        "required": True,
    },
    "age": {
        "type": int,
        "required": False,
    },
    "city": {
        "type": str,
        "required": False,
    }
})
def some_func(data: dict):
    pass
    
це означає що в словнику data, повинна бути обовязково пара з ключем id і name (тому що required=True),
додатково можуть бути пари з ключами age, city
якщо валідація даних не пройдена, згенерувати ексепшин ValidationError (ексепшин створити)

"""

""" Task 3
Написати декоратор marshal, його завдання перевірити на відповідність певній моделі, те що повертає функція

Приклад
@marshal({
    "id": {
        "type": int,
        "required": True,
    },
    "name": {
        "type": str,
        "required": True,
    },
    "age": {
        "type": int,
        "required": False,
    },
    "city": {
        "type": str,
        "required": False,
    },
    "new_messages_number": {
        "type": int,
        "required": True,
        "default": 0
    },
})
def some_func(*args, **kwargs) -> dict:
    return data

це означає що в словнику data, повинна бути обовязково пара з ключем id і name і new_messages_number (тому що required=True),
додатково можуть бути пари з ключами age, city
якщо в словнику new_messages_number ключа немає - то присвоїти значення яке записано в default
якщо валідація даних не пройдена, згенерувати ексепшин ValidationError
"""


""" ***
Додатково напишіть тести на кожне з завданнь
"""


