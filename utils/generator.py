import random


class UserDataGenerator:

    @staticmethod
    def generate_valid_email():
        return f"qwerty{random.randint(100,999)}@yandex.ru"

    @staticmethod
    def generate_valid_password():
        return f"Qwerty{random.randint(100,999)}"

    @staticmethod
    def generate_invalid_email():
        return f"qwerty{random.randint(100,999)}yandex.ru"
