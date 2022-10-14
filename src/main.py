import getpass

from password_manager import PasswordManager


def print_commands():
    print('''
====================
Commands:
1) Get all passwords
2) Get password
3) Save password
4) Delete password
5) Delete all passwords
====================
    ''')


def print_passwords_deleted():
    print('''
====================
All passwords deleted!
====================
    ''')


def print_login_and_password(login, password):
    print(f'''
====================   
Password for '{login}': {password}
====================  
    ''')


def print_password_saved(login):
    print(f'''
====================
Password for '{login}' successfully saved!
====================
    ''')


def print_password_deleted(login):
    print(f'''
====================
Password for '{login}' successfully deleted!
====================
    ''')


def get_login_from_user_input():
    return input('Enter login: ')


def get_password_from_user_input():
    return getpass.getpass('Enter password: ')


def main():
    password_manager = PasswordManager('../data/encrypted_passwords', '12345')

    print_commands()

    while True:
        print('Enter command number: ')
        command_number = int(input())

        if command_number == 1:
            passwords = password_manager.get_passwords()
            for login, password in passwords.items():
                print_login_and_password(login, password)
        elif command_number == 2:
            login = get_login_from_user_input()
            password = password_manager.get_password(login)
            print_login_and_password(login, password)
        elif command_number == 3:
            login = get_login_from_user_input()
            password = get_password_from_user_input()
            password_manager.save_password(login, password)
            print_password_saved(login)

        elif command_number == 4:
            login = get_login_from_user_input()
            password_manager.delete_password(login)
            print_password_deleted(login)

        elif command_number == 5:
            password_manager.delete_passwords()
            print_passwords_deleted()

        else:
            print_commands()


main()
