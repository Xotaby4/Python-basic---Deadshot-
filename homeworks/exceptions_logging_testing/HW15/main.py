import uuid
import datetime as dt

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
        if is_incoming:
            self.incoming_messages.append(message_obj)
        else:
            self.outgoing_messages.append(message_obj)

    def get_last_message(self):
        """
        Повертає останнє вхідне повідомлення
        :return:
        """
        return self.incoming_messages[-1]

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
        return {"incomings": self.incoming_messages if include_incoming else None,
                "outgoings": self.outgoing_messages if include_outgoing else None}

    def read_last_message(self):
        """
        повертає останнє повідомлення, саме повідомлення видаляється з incoming_messages
        :return:
        """
        return self.incoming_messages.pop()

    def read_all_messages(self):
        """
        повертає список всіх вхідних повідомлень, і очищає даний список
        :return:
        """
        tl = self.incoming_messages.copy()
        self.incoming_messages.clear()
        return tl

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
        self.text = new_text


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
        if user_from_id in UserHelper.users_db and user_to_id in UserHelper.users_db:
            user_from = UserHelper.get_user(user_from_id)
            user_to = UserHelper.get_user(user_to_id)
            message = Message(user_from, user_to, dt.datetime.now(), text)
            user_from.outgoing_messages.append(message)
            user_to.incoming_messages.append(message)
        else:
            raise UserNotFound

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
        user = User(name)
        cls.user_db[user.id] = user
        return user.id

    @classmethod
    def get_user(cls, id):
        """
        Повертає юзера, якщо юзера немає, генерує ексепшн
        :param id:
        :return:
        """
        if id in cls.users_db.keys():
            return cls.users_db[id]
        else:
            raise UserNotFound

    @classmethod
    def delete_user(cls, id):
        """
        Видаляє юзера з users_db
        :param id:
        :return:
        """
        del(cls.users_db[id])
pass