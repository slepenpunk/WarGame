import random


class ZooFerm:
    """
    Virtual ZooFerm
    This class can work with private attributes
    """
    critter_list = []
    dead_critters = []
    random_eat_words = ['Thank you!', 'It\'s so tasty!', 'MMMMM...']
    random_play_words = ['Weeee!', 'It\'s so fun!', 'I\'m happy!']
    total_deaths = 0

    def __init__(self, name, happy, hungry):
        self.__name = name
        self.__happy = happy
        self.__hungry = hungry
        self.__mood = 0
        self.dead = True

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

    # This method is on, when doing some action
    def __pass_time(self):
        self.__hungry += 1
        self.__happy += 1

    # Returns how critter feel self
    def moods(self):
        unhappiness = self.happy + self.hungry + self.mood
        if unhappiness <= 4:
            feel = 'great!'
        elif 4 < unhappiness <= 10:
            feel = 'good'
        elif 10 < unhappiness <= 16:
            feel = 'could be better...'
        elif 16 < unhappiness <= 22:
            feel = 'bad'
        elif unhappiness <= 25:
            feel = "if you don't do anything, I will die"
        else:
            feel = 'like dead:('
            ZooFerm.total_deaths += 1
            self.dead = False
            print(f'{self.name} is dead!')
        return feel

    # Print name and condition about critters
    def talk(self):
        if self.dead is True:
            print(f'My name is {self.name}, now i feel {self.moods()}')
            if self.hungry >= 4:
                print('I\'m feel hungry...')
            if self.happy >= 4:
                print("I'm bored...")
            self.__pass_time()
        else:
            ZooFerm.dead_critters.append(self)

    # Gives food to critters
    def eat(self, data):
        self.hungry = data
        reaction = random.choice(ZooFerm.random_eat_words)
        print(reaction)

    # Play with critters
    def play(self, data):
        self.happy = data
        reaction = random.choice(ZooFerm.random_play_words)
        print(reaction)

    def add_to_list(self, critter):
        ZooFerm.critter_list.append(critter)


def main():
    start = True
    while start is True:
        try:
            total = int(input('Welcome to your ZooFerm!\nHow many critters do you want add: '))
            if total in range(1, 11):
                for i in range(total):
                    name = input('Enter name: ')
                    random_happy = random.randint(0, 10)
                    random_hungry = random.randint(0, 10)
                    crit = ZooFerm(name, random_happy, random_hungry)
                    crit.add_to_list(crit)
                    start = False
            else:
                print('In ZooFerm can be minimum 1 and maximum 10 critters!')
        except ValueError:
            print('Only numbers!')
    choice = None
    while choice != '0':
        critters = ZooFerm.critter_list
        deaths = ZooFerm.total_deaths
        print(
            '''
            0 - Exit
            1 - Know your pet mood
            2 - Play with pet
            3 - Give the food
            4 - View a dead animals
            '''
        )
        choice = input('Enter option: ')
        if choice == '0':
            print('Bye!')
            break
        elif choice == '1':
            options = input('Talk to all or one animals: ').capitalize()
            if options == 'One':
                name = input('Enter name: ')
                found = False
                for crit in critters:
                    if name == crit.name:
                        crit.talk()
                        found = True
                if not found:
                    print('This animal not in Zooferm!')
            elif options == 'All':
                if critters:
                    for crit in critters:
                        crit.talk()
                    print(f'Dead animals:{deaths}')
                else:
                    print('You don\'t have animals on Ferm! ')
        elif choice == '2':
            try:
                time = int(input('Enter total time can you play with pet: '))
                if time in range(0, 6):
                    for i in critters:
                        critters[i].play(time)
                else:
                    print('Max total play time - 5!')
            except ValueError:
                print('Only numbers!')
        elif choice == '3':
            try:
                food = int(input('Enter total food can you give to pet: '))
                if food in range(0, 6):
                    for i in critters:
                        critters[i].eat(food)
                else:
                    print('Max total food given - 5!')
            except ValueError:
                print('Only numbers!')
        elif choice == '4':
            print('That all dead animals:')
            for crit in ZooFerm.dead_critters:
                print(crit.name)
        else:
            print('Unknown command!')


main()
