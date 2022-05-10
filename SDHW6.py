

class User:
    def __init__(self, login: str, phone: str, email: str):
        self.messages = []
        self.chats = []
        self.__login = login
        self.__phone = phone
        self.__email = email

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


class Message:
    def __init__(self, user: User, chat, type):
        self.__user = user
        self.__chat = chat
        self.__mtype = type

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def chat(self):
        return self.__chat

    @chat.setter
    def chat(self, chat):
        self.__chat = chat

    @property
    def mtype(self):
        return self.__type

    @user.setter
    def mtype(self, type):
        self.__type = type


class Video(Message):
    def __init__(self, user, chat, video):
        super().__init__(user, chat, 'Video')
        self.__video = video

    @property
    def video(self):
        return self.__video

    @video.setter
    def video(self, video):
        self.__video = video


class Text(Message):
    def __init__(self, user, chat, text):
        super().__init__(user, chat, 'Text')
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text


class Audio(Message):
    def __init__(self, user, chat, audio):
        super().__init__(user, chat, 'Audio')
        self.__audio = audio

    @property
    def text(self):
        return self.__audio

    @text.setter
    def text(self, audio):
        self.__audio = audio



class Chat:
    def __init__(self, chat_name: str):
        self.name = chat_name
        self.users = []
        self.messages = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def add_user(self, user: User):
        self.users.append(user)

    def add_message(self, message: Message):
        self.messages.append(message)


class Messenger:
    def __init__(self, messenger_name: str):
        self.name = messenger_name
        self.chats = {}
        self.users = []
        self.messages = []

    def add_chat(self, chat_name: str):
        if chat_name not in self.chats:
            new_chat = Chat(chat_name)
            self.chats[chat_name] = new_chat
        else:
            print("ERROR - Chat with such name already exists")

    def registrate_user(self, user: User):
        self.users.append(user)
        print(f"User {user.login} is registered in messenger {self.name}")

    def add_user_to_chat(self, user: User, chat_name: str):
        if chat_name not in self.chats:
            print("ERROR - Not exist chat with such name ")
        else:
            self.chats[chat_name].users.append(user)
            if user not in self.users:
                self.users.append(user)
                print(f"User {user.login} is registered in messenger {self.name}")
            user.chats.append(self.chats[chat_name])
            print(f'User {user.login} added in {chat_name}')

    def add_message(self, msg: Message):
        chat_name = msg.chat
        user = msg.user
        mtype = type(msg).__name__

        if chat_name in self.chats:
            if user in self.chats[chat_name].users:
                new_message = Message(user, chat_name, 'Text')
                self.messages.append(new_message)
                self.chats[chat_name].messages.append(new_message)
                user.messages.append(new_message)

                print(f'{chat_name}: {user.login} send {mtype.lower()} message')
            else:
                print(f"ERROR - User {user.login} is not in chat {chat_name}")
        else:
            print(f"ERROR - No chat with such name {chat_name}")

    def find_word_in_messages(self, word: str):
        counter = 0
        for mess in self.messages:
            if mess is Message:
                if word in mess.text:
                    counter += 1
        print(f'Word: {word} is found in messenger {self.name} - {counter} times')

    def shared_chats(self, *args):
        user_1 = args[0]
        if user_1 in self.users:
            r = set(user_1.chats)
            for user in args[1:]:
                if user in self.users:
                    r = r.intersection(user.chats)
                else:
                    print(f'User {user.login} is not registered in messenger {self.name}')
            print(f'Shared_chats:')
            for chat in r:
                print(chat.name)
        else:
            print(f'User {user_1.login} is not registered in messenger {self.name}')

    @staticmethod
    def compare_messengers(obj1, obj2):
        if (len(obj1.users) != len(obj2.users)) or \
                (len(obj1.chats) != len(obj2.chats)) or \
                (len(obj1.messages) != len(obj2.messages)):
            print(f'Messengers not equal')
            return False
        else:
            print(f'Messengers is equal')
            return True

    @staticmethod
    def get_from_messengers(obj1, obj2, subject: str, item: str):
        set1 = set()
        set2 = set()
        if item == 'phone':
            for user in obj1.users:
                set1.add(user.phone)
            for user in obj2.users:
                set2.add(user.phone)
        elif item == 'email':
            for user in obj1.users:
                set1.add(user.email)
            for user in obj2.users:
                set2.add(user.email)

        if subject == 'intersection':
            result = set1.intersection(set2)
        elif subject == 'difference':
            result = set1.difference(set2)
        elif subject == 'union':
            result = set1.union(set2)
        else:
            result = set()

        return result


if __name__ == '__main__':
    telega = Messenger('Tgram')

    telega.add_chat("MIPT_Students")
    telega.add_chat("MIPT_News")
    user1 = User('Alex', "+79149453676", "kingofIcq@gmail.com")
    user2 = User('Katya', "+79149462682", "kate1996@gmail.com")
    telega.registrate_user(user1)
    telega.add_user_to_chat(user1, 'MIPT_Students')
    telega.add_user_to_chat(user1, 'MIPT_News')
    telega.registrate_user(user2)
    telega.add_user_to_chat(user2, 'MIPT_Students')
    telega.add_user_to_chat(user2, 'MIPT_News')

    telega.add_message(Text(user1, 'MIPT_Students', 'Hello'))
    telega.add_message(Video(user1, 'MIPT_Students', 'Yes'))
    telega.add_message(Text(user2, 'MIPT_Students', 'No'))
    telega.add_message(Audio(user2, 'MIPT_Students', 'Yes'))