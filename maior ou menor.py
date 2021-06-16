fechado = False

while fechado == False:
    a = int(input('Insira o primeiro valor: '))
    b = int(input('Insira o segundo valor: '))

    if a == b:
        resultado = print("O número", a, "é igual a", b)
    elif a < b:
        resultado = print("O número", a, "é menor que", b)
    elif a > b:
        resultado = print("O número", a, "é maior que", b)
    else:
        resultado = print("Os dois números são diferentes.")

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True