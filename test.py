import pickle, shelve


class User():
    '''Create any users and dump it with help pickle'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f'Name - {self.name}\n'
                f'Age - {self.age}\n')

    @staticmethod
    def read_users():
        with open('Users.dat', 'rb') as f:
            while True:
                try:
                    load = pickle.load(f)
                    print(load)
                except EOFError:
                    break

    @staticmethod
    def dump_users(user):
        with open('Users.dat', 'ab') as f:
            pickle.dump(user, f)


def main():
    try:
        amount = int(input('Enter the amount you want to create: '))
        for i in range(amount):
            name = input('Enter name: ').capitalize()
            age = int(input('Enter age: '))
            user1 = User(name, age)
            print(f'\nCreate user:\n'
                  f'{user1}')
            User.dump_users(user1)
    except ValueError:
        print('You can enter only numbers!')

    print('All user in file:')
    User.read_users()


main()
