"""
Нижче представлений скелет системи по відправки повідомлень між двома юзерами
завдання 1
реалізувати методи як описано в докстрінгах до кожного з них
завдання 2,
написати тести на кожну з функцій
написати тести для особливих випадків, наприклад
відправити повідомлення для неіснуючого юзера (повинні отримати UserNotFound)
скасувати повідомлення а потім намагатись його отримати (повинні отримати MessageNotFound)

* завдання за бажанням
incoming_messages, outgoing_messages не зовсім зручно використовувати якщо це списки, наприклад для пошуку повідомлення по ід
переробити на словник також не зручно, тому що тоді не зручно отримувати останнє повідомлення

вирішення зробити incoming_messages і outgoing_messages як OrderedDict

"""


import uuid


class UserNotFound(Exception):
    pass


class MessageNotFound(Exception):
    pass


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.incoming_messages = []
        self.outgoing_messages = []

    def add_message(self, message_obj, is_incoming=True):
        """
        Додає повідомлення в incoming_messages чи outgoing_messages в залежності від is_incoming
        :param message_obj:
        :param is_incoming:
        :return:
        """
        # TODO implement it
        pass

    def get_last_message(self):
        """
        Повертає останнє вхідне повідомлення
        :return:
        """
        # TODO implement it
        pass

    def get_all_messages(self, include_incoming=True, include_outgoing=True):
        """
        Повертає словник виду
        {
            "incomings": list of messages, - за умови що include_incoming True, інакше None
            "outgoings": list of messages, - за умови що include_outgoing True, інакше None
        }

        :param include_incoming:
        :param include_outgoing:
        :return:
        """
        # TODO implement it
        pass

    def read_last_message(self):
        """
        повертає останнє повідомлення, саме повідомлення видаляється з incoming_messages
        :return:
        """
        # TODO implement it
        pass

    def read_all_messages(self):
        """
        повертає список всіх вхідних повідомлень, і очищає даний список
        :return:
        """
        # TODO implement it
        pass

    def get_message_by_id(self, message_id, include_incoming=True, include_outgoing=True):
        """
        знайти повідомлення по його ід, include_incoming, include_outgoing визначають в якому контейнері шукати
        якщо повідомлення немає, згенерувати ексепшин MessageNotFound
        :param message_id:
        :param include_incoming:
        :param include_outgoing:
        :return:
        """


class Message:
    def __init__(self, user_from, user_to, date, text):
        self.id = uuid.uuid4()
        self.user_from = user_from
        self.user_to = user_to
        self.date = date
        self.text = text

    def edit(self, new_text):
        """
        змінює текст повідомлення
        :return:
        """
        # TODO implement it
        pass


class MessageHelper:
    @staticmethod
    def send_message(user_from_id, user_to_id, text):
        """
        створює обєкт повідомлення
        записує цей обєкт в вхідні повідомлення для user_to, і в вихідні для user_from
        Важливо! перевірити чи юзери існують в базі даних
        :param user_from_id:
        :param user_to_id:
        :param text:
        :return:
        """
        # TODO - create message object
        # TODO = save message to user user_to
        pass

    @staticmethod
    def unsend_message(message):
        """
        Видаляє повідомлення у двох юзерів
        :param message:
        :return:
        """
        # TODO - create message object
        # TODO = save message to user user_to
        pass


class UserHelper:
    users_db = {

    }

    @classmethod
    def create_user(cls, name):
        """
        створює юзера записує його в users_db, повертає ід юзера
        приклад
            user_db[user.id] = user
        :param name:
        :return:
        """
        # TODO implement it

    @classmethod
    def get_user(cls, id):
        """
        Повертає юзера, якщо юзера немає, генерує ексепшн
        :param id:
        :return:
        """
        # TODO implement it

    @classmethod
    def delete_user(cls, id):
        """
        Видаляє юзера з users_db
        :param id:
        :return:
        """
        # TODO implement it




