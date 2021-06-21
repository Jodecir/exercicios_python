fechado = False

while fechado == False:
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))

    if n1 == n2:
        resultado = print("O número", n1, "é igual a", n2)
    elif n1 < n2:
        resultado = print("O número", n1, "é menor que", n2)
    elif n1 > n2:
        resultado = print("O número", n1, "é maior que", n2)
    else:
        resultado = print("Os dois números são diferentes.")

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True