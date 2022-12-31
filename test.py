import sys


class Puppy:
    """
    Virtual tamagotchi
    This class can work with private attributes
    """

    def __init__(self, name, happy=0, hungry=0):
        self.__name = name
        self.__happy = happy
        self.__hungry = hungry
        self.__mood = 0

    @property
    def hungry(self):
        return self.__hungry

    @property
    def name(self):
        return self.__name

    @property
    def happy(self):
        return self.__happy

    @property
    def mood(self):
        return self.__mood

    @happy.setter
    def happy(self, data):
        self.__happy -= data
        if self.__happy < 0:
            self.__happy = 0
        self.__pass_time()

    @hungry.setter
    def hungry(self, data):
        self.__hungry -= data
        if self.__hungry < 0:
            self.__hungry = 0
        self.__pass_time()

    def __pass_time(self):
        self.__hungry += 1
        self.__happy += 1

    def moods(self):
        unhappiness = self.happy + self.hungry + self.mood
        if unhappiness <= 4:
            feel = 'great!'
        elif 4 < unhappiness <= 10:
            feel = 'good!'
        elif 10 < unhappiness <= 16:
            feel = 'could be better...'
        elif 16 < unhappiness <= 22:
            feel = 'bad'
        else:
            if unhappiness <= 25:
                feel = "if you don't do anything now, I will die"
            else:
                print('Сongratulations! You killed Deda;(')
                sys.exit()
        return feel

    def talk(self):
        print(f'My name is {self.name}, now i feel {self.moods()}')
        print('Happy', self.happy, 'Hungry', self.hungry)
        if self.hungry >= 4:
            print("i'm feeling hungry!")
        if self.happy >= 4:
            print("I'm bored...")
        self.__pass_time()

    def eat(self, data):
        self.hungry = data
        print("It's so tasty!")

    def play(self):
        self.happy = 4
        print('YYYUUUEEE!!!')


def main():
    set_name = input('Enter name: ')
    p1 = Puppy(set_name)
    choice = None
    while choice != '0':
        print(
            '''
            0 - Exit
            1 - Know your pet mood
            2 - Play with pet
            3 - Give the food
            '''
        )
        choice = input('Enter option: ')
        if choice == '0':
            print('Bye!')
            break
        elif choice == '1':
            p1.talk()
        elif choice == '2':
            p1.play()
        elif choice == '3':
            try:
                food = int(input('Enter total food can you give to pet: '))
                if food in range(0, 6):
                    p1.eat(food)
                else:
                    print('Max total food given - 5!')
            except ValueError:
                print('Only numbers!')
        else:
            print('Unknown command!')


main()
