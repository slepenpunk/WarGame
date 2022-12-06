# Create cats with different specifications of name, color, mood and age.
import random


class Cats():
    """Create different cats"""
    cats_dict = {}
    _total = 0
    names = ('Choma', 'Kevin', 'Bastard', 'Kitty')
    colors = ['White', 'Black', 'Gray', 'Brown']
    moods = ('凸(￣ヘ￣)', '٩(ఠ益ఠ)۶', '(▽◕ ᴥ ◕▽)', '(´｡• ᵕ •｡)')

    @classmethod
    def total_cats(cls):
        print('Total cats:', cls._total)

    @classmethod
    def add_colors(cls, color):
        new = cls.colors.append(color)
        return new

    @classmethod
    def random_cat(cls):
        color = random.choice(cls.colors)
        mood = random.choice(cls.moods)
        age = random.randint(1, 20)
        name = random.choice(cls.names)
        return cls(color, mood, age, name)

    @classmethod
    def find_cat_by_name(cls):
        c_dict = cls.cats_dict
        find_name = input('Enter name to find a cat: ').capitalize()
        if find_name in c_dict:
            for i in c_dict.values():
                print(f'{find_name}\n'
                      f'Color - {i[0]}\n'
                      f'Age - {i[1]}\n'
                      f'Mood - {i[2]}\n')
        else:
            print('There is no such cat!')

    def __init__(self, color, mood, age, name):
        self.color = color
        self.mood = mood
        self.age = age
        self.name = name
        c_dict = Cats.cats_dict
        c_dict[name] = color, age, mood
        Cats._total += 1

    def __str__(self):
        rep = (f'\nA new cat has been created!\n'
               f'Name - {self.name}\n'
               f'Color - {self.color}\n'
               f'Mood - {self.mood}\n'
               f'Age - {self.age}')
        return rep


def main():
    colors = Cats.colors
    choice = None
    while choice != '0':
        print(
            '''
            0 - Exit
            1 - Create cats
            2 - View total cats
            3 - View the colors of cats
            4 - Add color
            5 - Delete color
            6 - Find a cat by name
            ''')
        choice = input('Enter your choice: ')
        if choice == '0':
            break
        elif choice == '1':
            try:
                c = int(input('Enter how many cats you want to create: '))
                if c <= 20:
                    if colors:
                        for i in range(c):
                            print(Cats.random_cat())
                    else:
                        print('No colors!')
                else:
                    print('Max 20 cats at a time!')
            except ValueError:
                print('Enter only numbers!')
        elif choice == '2':
            Cats.total_cats()
        elif choice == '3':
            for i in colors:
                print(i)
        elif choice == '4':
            new_color = input('Enter color new color: ').capitalize()
            Cats.add_colors(new_color)
            print('Color', new_color, 'was been added!')
        elif choice == '5':
            delete_color = input('Enter color which you want delete: ').capitalize()
            if delete_color in colors:
                colors.remove(delete_color)
                print('Color', delete_color, 'was been deleted!')
            else:
                print('No such is color!')
        elif choice == '6':
            Cats.find_cat_by_name()
        else:
            print('Unknown command!')


main()
