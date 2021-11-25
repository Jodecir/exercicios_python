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
            resultado = print("O número", n1, "é negativo.")
        elif n1 > 0:
            resultado = print("O número", n1, "é positivo.")
        else:
            resultado = print("O número", n1, "é neutro.")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True