import json

from cryptography.fernet import Fernet


class PasswordManager:

    def __init__(self, password_json_file_path, key):
        self.password_json_file_path = password_json_file_path
        self.key = key

    def _encrypt_passwords(self, passwords):
        with open(self.password_json_file_path, 'wb') as password_json_file:
            fernet = Fernet(self.key)
            password_json_file.write(fernet.encrypt(bytes(json.dumps(passwords))))

    def _decrypt_passwords(self):
        with open(self.password_json_file_path, 'rb') as password_json_file:
            fernet = Fernet(self.key)
            passwords = json.loads(fernet.decrypt(str(password_json_file.read())))

            return passwords

    def save_password(self, login, password):
        pass

    def get_password(self, login):
        pass

    def get_passwords(self):
        pass

    def delete_password(self, login):
        pass

    def delete_passwords(self):
        pass



