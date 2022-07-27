from unittest import TestCase
import datetime as dt
import main


class TestUser(TestCase):
    def setUp(self) -> None:
        self.user_from = main.User("UserFrom")
        self.user_to = main.User("UserTo")
        self.message = main.Message(self.user_from, self.user_to, dt.datetime.now(), 'test message')
        self.message1 = main.Message(self.user_to, self.user_from, dt.datetime.now(), 'test message1')
        self.message2 = main.Message(self.user_from, self.user_to, dt.datetime.now(), 'test message2')
        for mes in [self.message, self.message1, self.message2]:
            self.user_to.add_message(mes)

    def tearDown(self) -> None:
        del (self.user_from, self.user_to, self.message)

    def test_add_in(self):
        self.user_to.add_message(self.message)
        self.assertIn(self.message, self.user_to.incoming_messages)

    def test_add_out(self):
        self.user_to.add_message(self.message1, False)
        self.assertIn(self.message1, self.user_to.outgoing_messages)

    def test_get_last(self):
        self.assertEqual(self.user_to.incoming_messages[-1], self.message2)

    def test_get_all(self):
        self.assertEqual(self.user_to.get_all_messages(True, True), {"incomings": [self.message, self.message2],
                                                                     "outgoings": [self.message1]})
        self.assertEqual(self.user_to.get_all_messages(False, True), {"incomings": None,
                                                                     "outgoings": [self.message1]})

    def test_read_last(self):
        self.assertEqual(self.user_to.read_last_message(), self.message2)
        self.assertEqual(self.user_to.incoming_messages[-1], self.message)

    def test_read_all(self):
        self.assertEqual(self.user_to.read_all_messages(), [self.message, self.message2])
        self.assertEqual(self.user_to.incoming_messages, [])

    def test_get_by_id(self):
        self.assertEqual(self.user_to.get_message_by_id(self.message.id), self.message)

class TestMessage(TestCase):
    def setUp(self) -> None:
        self.user_from = main.User("UserFrom")
        self.user_to = main.User("UserTo")
        self.message = main.Message(self.user_from, self.user_to, dt.datetime.now(), 'test message')

    def tearDown(self) -> None:
        del (self.user_from, self.user_to, self.message)

    def test_edit(self):
        self.message.edit("new text")
        self.assertEqual(self.message.text, "new text")

class TestMessageHelper(TestCase):
    def setUp(self) -> None:
        self.user_from_id = main.UserHelper.create_user("UserFrom")
        self.user_to_id = main.UserHelper.create_user("UserTo")
        self.user_to = main.UserHelper.get_user(self.user_to_id)
        main.MessageHelper.send_message(self.user_from_id, self.user_to_id, "Hello bro")
        self.message = self.user_to.get_last_message()

    def tearDown(self) -> None:
        del (self.user_from_id, self.user_to_id)

    def test_send_message(self):
        self.assertEqual(main.UserHelper.get_user(self.user_to_id).get_last_message().text,
                         "Hello bro")
        self.assertEqual(main.UserHelper.get_user(self.user_from_id).outgoing_messages[-1].text,
                         "Hello bro")
        us = main.User("Fail")
        with self.assertRaises(main.UserNotFound):
            main.MessageHelper.send_message(self.user_from_id, us.id, "UDP")

    def test_unsend_message(self):
        m_id = self.message.id
        main.MessageHelper.unsend_message(self.message)
        with self.assertRaises(main.MessageNotFound):
            self.user_to.get_message_by_id(m_id)

class TestUserHelper(TestCase):
    def setUp(self) -> None:
        self.uh = main.UserHelper
        self.user_id = self.uh.create_user("Messagesender")

    def tearDown(self) -> None:
        del(self.uh)

    def test_create_user(self):
        self.assertIn(self.user_id, self.uh.users_db)

    def test_get_user(self):
        self.assertEqual(self.uh.get_user(self.user_id).name, "Messagesender")

    def test_delete_user(self):
        self.uh.delete_user(self.user_id)
        with self.assertRaises(main.UserNotFound):
            self.uh.get_user(self.user_id)


