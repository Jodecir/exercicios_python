class Television:
    def __init__(self):
        self.state = False
        self.channel = 4

    def power(self):
        if self.state:
            self.state = False
        else:
            self.state = True

    def next_channel(self):
        if self.state:
            self.channel += 1

    def previous_channel(self):
        if self.state and self.channel >= 1:
            self.channel -= 1

if __name__ == '__main__':
    tv = Television()
    print('A TV está ligada: {}'.format(tv.state))
    tv.next_channel()
    print('Canal: {}'.format(tv.channel))
    tv.previous_channel()
    print('Canal: {}'.format(tv.channel))
    tv.power()
    print('A TV está ligada: {}'.format(tv.state))
    tv.next_channel()
    print('Canal: {}'.format(tv.channel))
    tv.previous_channel()
    print('Canal: {}'.format(tv.channel))
    tv.previous_channel()
    print('Canal: {}'.format(tv.channel))
    tv.previous_channel()
    print('Canal: {}'.format(tv.channel))
    tv.previous_channel()
    print('Canal: {}'.format(tv.channel))
    tv.power()
    print('A TV está ligada: {}'.format(tv.state))
    tv.previous_channel()
    print('Canal: {}'.format(tv.channel))