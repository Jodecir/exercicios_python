def pulaLinha():
    print("---------------------")

fechado = False

while fechado == False:
    try:
        n1 = int(input("Digite um número: "))
    except FloatingPointError: 
        print("Valores flutuantes são inválido, digite apenas números inteiros.")
    except ValueError:
        print("Valor inválido, digite apenas números.")
    else:
        if __name__ == '__main__':
            if n1 % 2 == 0:
                pulaLinha()
                print("Número Par")
                pulaLinha()
            elif n1 % 2 == 1:
                pulaLinha()
                print("Número Ímpar")
                pulaLinha()
            else:
                pulaLinha()
                print("Valor Inválido")
                pulaLinha()
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True