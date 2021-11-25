fechado = False

while fechado == False:
    try:
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
    except FloatingPointError:
        print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        if n1 == n2:
            resultado = print("O número", n1, "é igual a", n2)
        elif n1 < n2:
            resultado = print("O número", n1, "é menor que", n2)
        elif n1 > n2:
            resultado = print("O número", n1, "é maior que", n2)
        else:
            resultado = print("O número", n1, "é diferente de", n2)
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True