class Television:
    """Simulator TV"""
    channels = {1: 'Первый кАнал',
                2: 'Россия 88',
                3: 'Матч ТВ',
                4: 'Спаси и Сохрани',
                5: 'ТНТ',
                6: 'СТС',
                7: 'Карусель',
                8: 'Brazzers Elite',
                9: '2x2',
                10: 'MTV'}

    def __init__(self):
        self.volume = []
        self.cur_channel = 1

    def set_channel(self, number):
        """Choice a channel from available channels"""
        if number in self.channels:
            self.cur_channel = number
            return f'CHANNEL - {number}\n' \
                   f'NAME - {self.channels[number]}'
        else:
            return 'No such this channel!'

    def set_volume(self, level):
        """Change volume by press + or -"""
        if level == '+' and len(self.volume) < 10:
            self.volume.append('|')
        elif level == '-' and len(self.volume) > 0:
            self.volume.pop()
        elif level not in ['+', '-']:
            return 'Unknown command!'
        else:
            return 'Range 0-10!'
        return f'Current volume - {self.volume}'

    def info(self):
        rep = f'VOLUME - {self.volume}\n' \
              f'CHANNEL - {self.cur_channel}: {self.channels[self.cur_channel]}'
        return rep

    def add_channel(self, name):
        if name not in self.channels.values():
            chan = list(self.channels.keys())
            chan.sort()
            number = chan[-1]
            self.channels[number + 1] = name
        else:
            return 'This channel is already exist!'
        return f'Channel - {name} added!'


def main():
    tv = Television()
    choice = None
    while choice != '0':
        print('''
        0 - Turn off
        1 - Change channel
        2 - Change volume
        3 - View info
        4 - Add channel
        ''')
        choice = input('Enter option: ')
        if choice == '0':
            print('Turn off')
            break
        elif choice == '1':
            channel = int(input('Enter channel: '))
            ch = tv.set_channel(channel)
            print(ch)
        elif choice == '2':
            volume = input('Press +/- to change a volume: ')
            print(tv.set_volume(volume))
        elif choice == '3':
            print(tv.info())
        elif choice == '4':
            new_channel = input('Enter new name of channel: ')
            print(tv.add_channel(new_channel))
        else:
            print('Unknown option!')


main()
