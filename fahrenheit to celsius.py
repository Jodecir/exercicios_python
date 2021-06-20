fechado = False

while fechado == False:
    a = int(input('Insira o valor: '))
    escala = input('Insira a escala que ele está entre (F/C): ')
    c = (a - 32) / 1.8
    f = a * 1.8 + 32
        
    if __name__ == '__main__':
        if escala == "C" or escala == "c":
            print("A temperatura em F é", f,"°")
        elif escala == "F" or escala == "f":
            print("A temperatura em C é", c,"°")
        else:
            print("Repita o processo por favor , algo está incorreto.")

        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True