fechado = False

while fechado == False:
    try:
        lado1 = int(input("Digite a medida do lado 1: "))
        lado2 = int(input("Digite a medida do lado 2: "))
        lado3 = int(input("Digite a medida do lado 3: "))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        if __name__ == '__main__':
            if lado1 == lado2 & lado2 == lado3:
                print("---------------------")
                print("Equilátero")
                print("---------------------")
            elif lado1 == lado2 & lado3 != lado1:
                print("---------------------")
                print("Isóscele")
                print("---------------------")
            elif lado1 != lado2 != lado3:
                print("---------------------")
                print("Escaleno")
                print("---------------------")
            else:
                print("---------------------")
                print("Valor Inválido")
                print("---------------------")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True