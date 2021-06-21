fechado = False

while fechado == False:
    n1 = int(input('Insira o valor: '))

    if n1 < 0:
        resultado = print("O número", n1, "é negativo.")
    elif n1 > 0:
        resultado = print("O número", n1, "é positivo.")
    else:
        resultado = print("O número", n1, "é neutro.")

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True