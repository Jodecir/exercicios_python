fechado = False

while fechado == False:
    a = int(input('Insira o valor: '))

    if a < 0:
        resultado = print("O número", a, "é negativo.")
    elif a > 0:
        resultado = print("O número", a, "é positivo.")
    else:
        resultado = print("O número", a, "é neutro.")

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True