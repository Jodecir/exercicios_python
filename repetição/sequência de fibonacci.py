fechado = False

while fechado == False:
    try:
        qt = int(input("Insira a quantidade de números a serem gerados: "))
        n1 = int(input("Insira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        print("Sequência: {}, {}, ".format(n1,n2), end="")

        cont = 3

        while cont <= qt:
            sucessor = n1 + n2
            print ("{}, ".format(sucessor),end="")
            n1 = n2
            n2 = sucessor
            cont +=1
    finally:
        print("\n---------------------")
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True