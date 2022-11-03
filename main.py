# Create cats with different specifications of color, mood and age.
import random


class Cats():
    """Create different cats"""
    _total = 0
    colors = ['White', 'Black', 'Gray', 'Brown']
    moods = ('凸(￣ヘ￣)', '٩(ఠ益ఠ)۶', '(▽◕ ᴥ ◕▽)', '(´｡• ᵕ •｡)')

    @staticmethod
    def total_cats():
        print('Total cats:', Cats._total)

    @staticmethod
    def add_colors(color):
        new = Cats.colors.append(color)
        return new

    # @classmethod
    # def random_cat(cls):
    #     color = random.choice(cls.colors)
    #     mood = random.choice(cls.moods)
    #     age = random.randint(1, 20)
    #     return cls(color, mood, age)

    @staticmethod
    def random_cat():
        c = random.choice(Cats.colors)
        m = random.choice(Cats.moods)
        a = random.randint(1, 20)
        return Cats(c, m, a)

    def __init__(self, color, mood, age):
        self.color = color
        self.mood = mood
        self.age = age
        Cats._total += 1

    def __str__(self):
        rep = (f'\nA new cat has been created!\n'
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
            ''')
        choice = input('Enter your choice: ')
        if choice == '0':
            break
        elif choice == '1':
            try:
                c = int(input('Enter how many cats you want to create: '))
                if colors:
                    for i in range(c):
                        print(Cats.random_cat())
                else:
                    print('No colors!')
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
        else:
            print('Unknown command!')


main()