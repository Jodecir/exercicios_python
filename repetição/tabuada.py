def pulaLinha():
    print("---------------------")

fechado = False

while fechado == False:
    try:
        n1 = int(input("Insira o número: "))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        print("Tabuada de {}:".format(n1))
        n2 = 1
        count = 1
        while count != 11:
            print("{} x {:2} = {}".format(n1, n2, (n1 * n2)))
            count += 1
            n2 +=1
    finally:
        pulaLinha()
        repetir = input("Deseja continuar (s/n): ")

        if repetir == "n":
            fechado = True