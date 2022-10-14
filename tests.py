import unittest


class PasswordManagerTest(unittest.TestCase):

    def setUp(self):
        password_manager_key = 'Ar1Vider4I'

        self.password_json_file_path = 'data/encrypted_password.json'
        self.login = 'pavelihno'
        self.password = 'test_password'
        self.password_manager = PasswordManager(self.password_json_file_path, password_manager_key)

    def test_getting_passwords(self):
        self.password_manager.delete_passwords()

        extra_login = 'pavelihno_2'
        extra_password = 'test_password_2'

        self.password_manager.save_password(self.login, self.password)
        self.password_manager.save_password(extra_login, extra_password)

        self.assertDictEqual(
            self.password_manager.get_passwords(), {self.login: self.password, extra_login: extra_password}
        )

    def test_deleting_passwords(self):
        self.password_manager.delete_passwords()

        self.assertDictEqual(self.password_manager.get_passwords(), {})

    def test_deleting_password_by_login(self):
        self.password_manager.delete_passwords()

        self.password_manager.save_password(self.login, self.password)
        self.password_manager.delete_password(self.login)

        self.assertEqual(self.password_manager.get_password(self.login), None)

    def test_getting_password_by_non_existing_login(self):
        self.password_manager.delete_passwords()

        self.assertEqual(self.password_manager.get_password(self.login), None)

    def test_getting_password_by_existing_login(self):
        self.password_manager.delete_passwords()

        self.password_manager.save_password(self.login, self.password)

        self.assertEqual(self.password_manager.get_password(self.login), self.password)

    def test_getting_password_by_non_existing_login_when_wrong_password_manager_key_entered(self):
        self.password_manager.delete_passwords()

        self.password_manager.key = 'wrong_key'

        self.assertEqual(self.password_manager.get_password(self.login), None)

    def test_getting_password_by_existing_login_when_wrong_password_manager_key_entered(self):
        self.password_manager.delete_passwords()

        self.password_manager.key = 'wrong_key'

        self.assertEqual(self.password_manager.get_password(self.login), None)

    def test_deleting_password_by_login_when_wrong_password_manager_key_entered(self):
        self.password_manager.delete_passwords()

        self.password_manager.save_password(self.login, self.password)

        self.password_manager.key = 'wrong_key'

        self.assertDictEqual(self.password_manager.get_password(self.login), {self.login: self.password})


if __name__ == '__main__':
    unittest.main()
