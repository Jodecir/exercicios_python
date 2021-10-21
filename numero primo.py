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
                    print("Número primo")
                    break
                else:
                    print("Número não primo")
                    break
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True