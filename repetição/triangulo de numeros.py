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

fechado = False

while fechado == False:
    try:
        valorFinal = int(input("Insira um número que será o fim do triângulo: "))
    except FloatingPointError:
        print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        criarTrianguloRetangulo(valorFinal)
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True