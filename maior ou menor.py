fechado = False

while fechado == False:
    a = int(input('Insira o primeiro valor: '))
    b = int(input('Insira o segundo valor: '))

    if a == b:
        resultado = print("Os dois números são iguais.")
    elif a < b:
        resultado = print("O primeiro valor é menor que o segundo.")
    elif a > b:
        resultado = print("O primeiro valor é maior que o segundo.")
    else:
        resultado = print("Os dois números são diferentes.")

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True