import base64
import json
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ENCODING = 'utf-8'


class PasswordManager:

    def __init__(self, password_json_file_path, key):
        self.password_json_file_path = password_json_file_path
        self.key = None

        self.set_key(key)

    def set_key(self, key):
        salt = os.urandom(16)
        backend = default_backend()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=backend
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(key.encode(ENCODING)))

    def _encrypt_passwords(self, passwords):
        with open(self.password_json_file_path, 'wb') as password_json_file:
            fernet = Fernet(self.key)
            password_json_file.write(fernet.encrypt(json.dumps(passwords).encode(ENCODING)))

    def _decrypt_passwords(self):
        with open(self.password_json_file_path, 'rb') as password_json_file:
            fernet = Fernet(self.key)
            text = password_json_file.read()
            if text:
                return json.loads(fernet.decrypt(text.decode(ENCODING)))
            else:
                return {}

    def save_password(self, login, password):
        passwords = self.get_passwords()
        passwords[login] = password
        self._encrypt_passwords(passwords)

    def get_password(self, login):
        return self.get_passwords().get(login)

    def get_passwords(self):
        return self._decrypt_passwords()

    def delete_password(self, login):
        pass

    def delete_passwords(self):
        open(self.password_json_file_path, 'w').close()



