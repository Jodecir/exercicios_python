fechado = False

while fechado == False:
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
    operador = input('Insira o operador entre (+-/*) qualquer outro valor resultará em média: ')
    media = int((n1 + n2) / 2)

    if operador == "+":
        operacao = n1 + n2
    elif operador == "-":
        operacao = n1 - n2
    elif operador == "*":
        operacao = n1 * n2
    elif operador == "/":
        operacao = n1 / n2
    else:
        operacao = "Média igual a " + str(media)

    print("Resultado:")
    print(operacao)

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True