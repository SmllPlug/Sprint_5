from utils.generator import UserDataGenerator


def generate_valid_email():
    return UserDataGenerator.generate_valid_email()


def generate_valid_password():
    return UserDataGenerator.generate_valid_password()


def generate_invalid_email():
    return UserDataGenerator.generate_invalid_email()