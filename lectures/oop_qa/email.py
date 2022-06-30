class AuthError(Exception):
    def __init__(self):
        message = 'Authentication is failed. Wrong credentials'
        super().__init__(message)  # Exception(message)


class EmailFormatter:
    def __init__(self, message):
        self.message = message

    def full_formatter(self):
        return self.message

    def short_formatter(self):
        return self.message.strip()[:10]

    def default_formatter(self):
        return self.message.strip()

    def __call__(self, email_type=''):
        if email_type == 'full':
            return self.full_formatter()
        elif email_type == 'short':
            return self.short_formatter()
        else:
            return self.default_formatter()


class EmailSender:
    def __init__(self, login, password):
        self._email = login
        self._password = password
        self.debug_mode = False
        self._service = 'common'

    def _authenticate(self):
        #  .....
        if self._email == 'admin@admin.com' and self._password == 'test':
            return True

        raise AuthError()

    def _prepare_message(self, message):
        formatter = EmailFormatter(message)
        return formatter()

    def _send_message(self, message, receiver_email):
        print(f'Message {message} was sent to {receiver_email}')

    def prepare_and_send(self, message, receiver_email):
        if self._authenticate():
            prepared_message = self._prepare_message(message)
            self._send_message(prepared_message, receiver_email)

    def get_email_service(self):
        print(f'Email service is {self._service}')


def prepare_and_send(email, password, message, receiver_email):
    if email == 'admin@admin.com' and password == 'test':
        prepared_message = message.strip()
        print(f'Message {prepared_message} was sent to {receiver_email}')
    else:
        raise Exception('Authentication is failed. Wrong credentials')


class GmailEmailSender(EmailSender):
    def __init__(self, login, password):
        super().__init__(login, password)
        self._service = 'gmail'

    def _authenticate(self):
        if self._email.endswith('gmail.com') and \
                self._email == 'admin@gmail.com' and \
                self._password == 'custom_gmail':
            return True

        raise AuthError()


sender = EmailSender('admin@admin.com', 'test')
print(sender.__dict__)
# gmail_sender = GmailEmailSender('admin@gmail.com', 'custom_gmail')
# print(sender.debug_mode)
# EmailSender.prepare_and_send(sender, 'another message', 'pavlo@ukr.bet')
# print(type(sender))
# sender.prepare_and_send('     Hello, Andrii    ', 'andrii@gmail.com')
# gmail_sender.prepare_and_send('     Hello, Andrii    ', 'andrii@gmail.com')


