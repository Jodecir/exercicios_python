def pulaLinha():
    print("---------------------")

fechado = False

while fechado == False:
    variavel = str(input("Digite algo: ")).strip()
    varDividida = variavel.split()
    
    pulaLinha()
    print("Primeiro Valor: {}".format(varDividida[0]))
    print("Ultimo Valor: {}".format(varDividida[len(varDividida)-1]))
    pulaLinha()
    print("Tem: {} caracteres (contando espaços)".format(len(variavel)))
    print("Tem: {} caracteres (sem espaços)".format(len(variavel) - variavel.count(' ')))
    pulaLinha()
    print("O tipo primitivo desse valor é {}".format(type(variavel)))
    print("Só tem espaços: {}".format(variavel.isspace()))
    pulaLinha()
    print("É alfabético: {}".format(variavel.isalpha()))
    print("É alfanumérico: {}".format(variavel.isalnum()))
    print("É um título: {}".format(variavel.istitle()))
    print("É um número: {}".format(variavel.isnumeric()))
    pulaLinha()
    print("É maiúscula: {}".format(variavel.isupper()))
    print("É minúsculo: {}".format(variavel.islower()))
    pulaLinha()

    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True