def pulaLinha():
    print("---------------------")

vogais = ["a","e","i","o","u"]

fechado = False

while fechado == False:
    variavel = str(input("Digite algo: ")).strip()
    variavelInvertida = variavel[::-1]
    varDividida = variavel.split()
    variavelFatiada = list(variavel)

    pulaLinha()
    print(f"Primeiro Valor: {varDividida[0]}")
    print("Ultimo Valor: {}".format(varDividida[len(varDividida)-1]))
    pulaLinha()
    print("O tipo primitivo desse valor é {}".format(type(variavel)))
    if variavel == variavelInvertida:
        print("A variável é um palindromo.")
        pulaLinha()
    else:
        print("A variável não é um palindromo.")
    if len(variavel) == 1:
        print("Só contém 1 caractere.")
        pulaLinha()
    else:
        print("Contém: {} caracteres (contando espaços)".format(len(variavel)))
        print("Contém: {} caracteres (sem espaços)".format(len(variavel) - variavel.count(' ')))
        pulaLinha()
    if variavel.isspace():
        print("Só contém espaços no que você digitou.")
        pulaLinha()
    if variavel.isnumeric():
        print("Você digitou um número.")
        pulaLinha()
    if variavel.isalpha():
        print("Você digitou uma letra do alfabeto.")
        
        # variavelLower = variavel.lower()
        # vogaisTotal = 0
        # consoantesTotal = 0
        # for variavelLower in vogais:
        #     if variavelLower in vogais:
        #         vogaisTotal += 1
        #     else: 
        #         consoantesTotal += 1
        # print(f"Total de vogais digitados: {vogaisTotal}")
        # print(f"Total de consoantes digitados: {consoantesTotal}")

        pulaLinha()
    if variavel.isalnum():
        print("Você digitou algo alfanúmerico.")
        pulaLinha()
    else: 
        print("Você digitou algo que não é alfanúmerico.")
        pulaLinha()
    if variavel.istitle():
        print("Você digitou algo que se inicia com uma letra maiúscula.")
        pulaLinha()
    if variavel.isupper():
        print("Você digitou algo que contém uma letra maiúscula.")
        pulaLinha()
    if variavel.islower():
        print("Você digitou algo que contém uma letra minúscula.")
        pulaLinha()

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True