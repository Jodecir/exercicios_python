from typing import final

fechado = False

while fechado == False:
    try:
        n1 = int(input('Insira o valor: '))
    except FloatingPointError:
        print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        if n1 < 0:
            resultado = print(f"\n O número {n1} é negativo.\n")
        elif n1 > 0:
            resultado = print(f"\n O número {n1} é positivo.\n")
        else:
            resultado = print(f"\n O número {n1} é neutro.\n")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True