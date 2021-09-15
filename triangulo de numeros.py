fechado = False

while fechado == False:
    valorFinal = int(input("Insira um número que será o fim do triângulo: "))
    def criarTrianguloRetangulo(valor):
        if isinstance(valor, int):
            fileiraQt = 1
            while fileiraQt <= valor:
                valorInicial = 1
                texto = " "
                while valorInicial <= fileiraQt:
                    texto += str(valorInicial) + "\t"
                    valorInicial +=1
                print(texto)
                fileiraQt +=1
    criarTrianguloRetangulo(valorFinal)
    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True