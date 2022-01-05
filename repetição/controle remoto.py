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


tv = Television()
fechado = False

while fechado == False:
    botao = input("Deseja apertar o botão ON/OFF do controle (s/n): ")
    
    if __name__ == '__main__':    
        if botao == "s":
            tv.power()
            
            print("---------------------")
            print('A TV está ligada: {}'.format(tv.state))
            print('Canal: {}'.format(tv.channel))
            print("---------------------")
        else:
            botao = input("Deseja avançar ou retroceder o canal (+/-): ")

            if botao == "+":
                tv.next_channel()
                print('Canal: {}'.format(tv.channel))
            elif botao == "-":
                tv.previous_channel()
                print('Canal: {}'.format(tv.channel))
                
            print('A TV está ligada: {}'.format(tv.state))

            repetir = input("Deseja continuar com o controle na mão (s/n): ")
            if repetir == "n":
                fechado = True