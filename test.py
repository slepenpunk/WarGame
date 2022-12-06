class Television:
    """Simulator TV"""
    channels = {'1': 'Первый Анал',
                '2': 'Россия 88',
                '3': 'Матч ТВ',
                '4': 'Первый Анал',
                '5': 'Спаси и Сохрани',
                '6': 'ТНТ',
                '7': 'СТС',
                '8': 'Карусель',
                '9': 'Brazzers Elite',
                '10': '2x2',
                '11': 'MTV', }

    def __init__(self, volume=5):
        self.volume = volume

    @classmethod
    def set_channel(cls, number):
        """Choice a channel from available channels"""
        if number in cls.channels:
            return f'CHANNEL - {number}\n' \
                   f'NAME - {cls.channels[number]}'
        else:
            return 'No such this channel!'

    def set_volume(self, level):
        """Change volume by press + or -"""
        if self.volume in range(1, 10):
            if level == '+':
                self.volume += 1
            elif level == '-':
                self.volume -= 1
            else:
                return 'Unknown command!'
        else:
            if self.volume == 0:
                if level == '+':
                    self.volume += 1
                else:
                    return 'Volume range 0-10!'

            elif self.volume == 10:
                if level == '-':
                    self.volume -= 1
                else:
                    return 'Volume range 0-10!'

        return self.volume


    # def view_settings(self, channel):
    #     rep = f'{self.volume}\n' \
    #           f'{channel}'
    #     return rep


def main():
    tv = Television()
    choice = None
    while choice != '0':
        print('''
        0 - Turn off
        1 - Change channel
        2 - Change volume
        ''')
        choice = input('Enter option: ')
        if choice == '0':
            print('Turn off')
            break
        elif choice == '1':
            channel = input('Enter channel: ')
            ch = tv.set_channel(channel)
            print(ch)
        elif choice == '2':
            volume = input('Press +/- to change a volume: ')
            print(tv.set_volume(volume))


main()
