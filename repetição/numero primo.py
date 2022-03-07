def pulaLinha():
    print("---------------------")

fechado = False

while fechado == False:
    try:
        n1 = int(input("Digite um número: "))
    except FloatingPointError:
        print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        count = 1
        
        if __name__ == '__main__':
            while count <= n1:
                if n1 % 2 == 1 and n1 >= 2:
                    count = count + 1
                    pulaLinha()
                    print("Número primo")
                    pulaLinha()
                    break
                else:
                    pulaLinha()
                    print("Número não primo")
                    pulaLinha()
                    break
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True