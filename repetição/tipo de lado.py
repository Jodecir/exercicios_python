def pulaLinha():
    print("---------------------")

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
                pulaLinha()
                print("Equilátero")
                pulaLinha()
            elif lado1 == lado2 & lado3 != lado1:
                pulaLinha()
                print("Isóscele")
                pulaLinha()
            elif lado1 != lado2 != lado3:
                pulaLinha()
                print("Escaleno")
                pulaLinha()
            else:
                pulaLinha()
                print("Valor Inválido")
                pulaLinha()
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True